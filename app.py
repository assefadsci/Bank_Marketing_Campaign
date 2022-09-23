import pickle
from flask import Flask, request, render_template
import numpy as np

#create flask app
app= Flask(__name__)

#Load the pickle model
classifier= pickle.load(open('classifier.pkl', 'rb'))

# define homepage
@app.route('/', methods=['GET'])
def home():

        return render_template('index.html')
@app.route('/predict', methods=['POST'])

def predict():
    if request.method == 'POST':
        age= int(request.form['age'])
        balance = int(request.form['balance'])
        day = int(request.form['day'])
        duration= int(request.form['duration'])
        campaign = int(request.form['campaign'])
        pdays = int(request.form['pdays'])
        previous = int(request.form['previous'])

        #job
        job = request.form['job']  #not part fo the final process
        job_admin_ = 0
        if job_admin_ == job:
            job_admin_= 1
        else:
            job_admin_ = 0

        job_unknown = 0

        if job_unknown == job:
            job_unknown= 1
        else:
            job_unknown = 0

        job_unemployed= 0
        if job_unemployed == job:
            job_unemployed= 1
        else:
            job_unemployed = 0

        job_management= 0
        if job_management== job:
            job_management= 1
        else:
            job_management = 0

        job_housemaid= 0
        if job_housemaid== job:
            job_housemaid= 1
        else:
            job_housemaid = 0

        job_entrepreneur = 0
        if job_entrepreneur== job:
            job_entrepreneur= 1
        else:
            job_entrepreneur = 0

        job_student= 0
        if job_student== job:
            job_student= 1
        else:
            job_student = 0

        job_blue_collar= 0
        if job_blue_collar== job:
            job_blue_collar= 1
        else:
            job_blue_collar = 0

        job_self_employed = 0
        if job_self_employed== job:
            job_self_employed= 1
        else:
            job_self_employed = 0

        job_retired = 0
        if job_retired== job:
            job_retired= 1
        else:
            job_retired = 0

        job_technician= 0
        if job_technician== job:
            job_technician= 1
        else:
            job_technician = 0

        job_services =0
        if job_services== job:
            job_services= 1
        else:
            job_services = 0

        
        #marital status
        marital= request.form['marital'] 
        marital_divorced = 0
        if marital_divorced== marital:
            marital_divorced= 1
        else:
            marital_divorced = 0

        marital_married= 0
        if marital_married== marital:
            marital_married= 1
        else:
            marital_married = 0

        marital_single =0
        if marital_single== marital:
            marital_single= 1
        else:
            marital_single = 0
        
        # education
        education = request.form['education'] 
        education_primary = 0
        if education_primary== education:
            education_primary= 1
        else:
            education_primary = 0

        education_secondary= 0
        if education_secondary == education:
            education_secondary= 1
        else:
            education_secondary = 0

        education_tertiary =0
        if education_tertiary== education:
            education_tertiary= 1
        else:
            education_tertiary = 0

        education_unknown =0
        if education_unknown== education:
            education_unknown= 1
        else:
            education_unknown = 0

        # default
        default_yes= 0
        default_no = 0
        default = request.form['default'] 
        if default_yes == default:
            default_yes = 1
            default_no = 0
        else:
            default_yes = 0
            default_no = 1
        
        #Housing
        housing_yes= 0
        housing_no= 0
        housing = request.form['housing'] 
        if housing_yes == housing:
            housing_yes = 1
            housing_no = 0
        else:
            housing_yes = 0
            housing_no = 1
        
        #loan
        loan_yes= 0
        loan_no= 0
        loan = request.form['loan'] 
        if loan_yes == loan:
            loan_yes = 1
            loan_no= 0
        else:
            loan_yes = 0
            loan_no= 1
        
        #contact
        contact= request.form['contact'] 
        contact_cellular = 0
        if contact_cellular == contact:
            contact_cellular= 1
        else:
            contact_cellular = 0

        contact_telephone =0
        if contact_telephone== contact:
            contact_telephone= 1
        else:
            contact_telephone= 0

        contact_unknown=0
        if contact_unknown== contact:
            contact_unknown= 1
        else:
            contact_unknown = 0
        
        #month
        month = request.form['month']  
        month_apr = 0
        if month_apr== month:
            month_apr= 1
        else:
            month_apr = 0

        month_aug= 0
        if month_aug== month:
            month_aug= 1
        else:
            month_aug= 0

        month_dec =0
        if month_dec== month:
            month_dec= 1
        else:
            month_dec = 0

        month_feb =0
        if month_feb== month:
            month_feb= 1
        else:
            month_feb = 0

        month_jan = 0
        if month_jan== month:
            month_jan= 1
        else:
            month_jan= 0

        month_jul= 0
        if month_jul== month:
            month_jul= 1
        else:
            month_jul= 0

        month_jun =0
        if month_jun== month:
            month_jun= 1
        else:
            month_jun = 0

        month_mar =0
        if month_mar== month:
            month_mar= 1
        else:
            month_mar= 0 

        month_may = 0
        if month_may== month:
            month_may= 1
        else:
            month_may = 0 

        month_nov= 0
        if month_nov== month:
            month_nov= 1
        else:
            month_nov= 0 

        month_oct =0
        if month_oct== month:
            month_oct= 1
        else:
            month_oct= 0 

        month_sep =0
        if month_sep== month:
            month_sep= 1
        else:
            month_sep = 0
        
        #outcome
        poutcome = request.form['poutcome']
        poutcome_failure = 0
        if poutcome_failure== poutcome:
            poutcome_failure= 1
        else:
            poutcome_failure = 0 

        poutcome_other= 0
        if poutcome_other== poutcome:
            poutcome_other= 1
        else:
            poutcome_other= 0 

        poutcome_success =0
        if poutcome_success== poutcome:
            poutcome_success= 1
        else:
            poutcome_success= 0

        poutcome_unknown = 0
        if poutcome_unknown== poutcome:
            poutcome_unknown= 1
        else:
            poutcome_unknown = 0
        

        prediction= classifier.predict([[
        age, balance, day, duration, campaign, pdays, previous,job_admin_, job_blue_collar, job_entrepreneur,
         job_housemaid,job_management, job_retired, job_self_employed, job_services, job_student, job_technician,
        job_unemployed, job_unknown, marital_divorced, marital_married, marital_single, education_primary, 
        education_secondary, education_tertiary, education_unknown, default_no, default_yes, housing_no,
       housing_yes, loan_no, loan_yes, contact_cellular, contact_telephone, contact_unknown, month_apr, month_aug,
       month_dec, month_feb, month_jan, month_jul, month_jun, month_mar, month_may, month_nov, month_oct, month_sep,
       poutcome_failure, poutcome_other, poutcome_success,
       poutcome_unknown
        ]])
        
        return render_template('result.html', prediction= prediction)
    else:
        return render_template('index.html')
    
if __name__=='__main__':
    app.run(debug= True)
