
#Import Libraries
import pandas as pd 
from sklearn.utils import resample
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle


#Load train  and test dataset
train= pd.read_csv('bank-full.csv', sep=';')
test= pd.read_csv('bank.csv', sep=';')

#rename target variable
train.rename(columns={'y': 'subscribe'}, inplace= True)
test.rename(columns={'y': 'subscribe'}, inplace= True)

#label_encoding
label_encoder = LabelEncoder()

train['subscribe'] = label_encoder.fit_transform(train['subscribe'])
test['subscribe'] = label_encoder.fit_transform(test['subscribe'])

#handling extreme outliers
train= train[train['balance'] < 40000]

#Handling Imbalance Class
#Oversample minority class < subscribe == 'yes'>
yes= train[train['subscribe']== 1]
no= train[train['subscribe']== 0]

#oversample minority --yes
yes_oversampled = resample(yes, replace=True, n_samples=len(no), random_state=42) 

#combine majority and oversampled minority
train= pd.concat([yes_oversampled, no]).reset_index(drop=True)

#Split Dataset
X_train= train.drop('subscribe', axis= 1)
y_train= train['subscribe']
X_test= test.drop('subscribe', axis= 1)
y_test= test['subscribe']

#One-Hot Encoding
X_train= pd.get_dummies(X_train)
X_test= pd.get_dummies(X_test)

#Renaming the columsns by replacing special characters with underscore
X_train.columns = [ col.replace('.', '_') for col in X_train.columns]
X_train.columns = [ col.replace('-', '_') for col in X_train.columns]

X_test.columns = [ col.replace('.', '_') for col in X_test.columns]
X_test.columns = [ col.replace('-', '_') for col in X_test.columns]
#print(X_train.columns)
#Features Scaling
scaler= StandardScaler()

X_train= scaler.fit_transform(X_train)
X_test= scaler.transform(X_test)

#Random Forest Classifier
classifier = RandomForestClassifier(n_estimators=10)
classifier.fit(X_train, y_train)

#Serializing the model
pickle.dump(classifier, open('classifier.pkl', 'wb'))
