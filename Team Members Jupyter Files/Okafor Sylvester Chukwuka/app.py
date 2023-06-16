

import pickle
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from prediction import get_prediction, models, not_default_example, default_example
from sklearn.preprocessing import RobustScaler



st.set_page_config(page_title='Prosper LoanStatus Prediction App', page_icon="💱",
                               layout="wide", initial_sidebar_state='expanded')


# creating option list for dropdown menu

features = ['ListingNumber', 'ClosedDate', 'BorrowerAPR', 'BorrowerRate','DateCreditPulled', 'LoanMonthsSinceOrigination', 'LoanNumber',
       'LoanOriginationQuarter', 'LP_CustomerPayments','LP_CustomerPrincipalPayments']

st.markdown("<h1 style='color:white ;text-align: center;'>Prosper LoanStatus Prediction App 💸 </h1>", unsafe_allow_html=True)


def prediction(num):
    if num ==0:
        return "Loan is not Defaulted"
    else:
        return "Loan is Defaulted"


def main():
    with st.form('prediction_form'):

        st.header("Predict the input for following features:") 
        st.header("![Alt Text](https://th.bing.com/th/id/OIP.IdEAQWd4unaWF60q6Wni6AAAAA?pid=ImgDet&rs=1)")
        
        activities=['Logistic Regression','Naives Bayes', 'KNN', 'Decision Tree', 'Random Forest', 'Ada Boost']
        model_names = {name:model_name for name, model_name in zip(activities, models.keys())}
        option=st.sidebar.selectbox('Which model would you like to use?' ,activities)
        st.write('You selected:', option)
        st.subheader(option)

        DateCreditPulled = st.number_input('DateCreditPulled:', min_value=0, max_value=57331)
        LoanOriginationQuarter = st.number_input('LoanOriginationQuarter:', min_value=0, max_value=32)
      
        BorrowerAPR = st.number_input('BorrowerAPR:', min_value=0.0, max_value=0.6, step=1.,format="%.2f")
        BorrowerRate = st.number_input ( 'BorrowerRate:', min_value=0.0, max_value=0.5, step=1.,format="%.2f")
        EstimatedEffectiveYield = st.number_input('EstimatedEffectiveYield:', min_value=-0.2, max_value=0.4, step=1.,format="%.2f")
        EstimatedReturn = st.number_input('EstimatedReturn:', min_value=-0.2, max_value=0.4, step=1.,format="%.2f")
        LoanMonthsSinceOrigination = st.number_input('LoanMonthsSinceOrigination:', min_value=0, max_value=100)
        MonthlyLoanPayment = st.number_input('MonthlyLoanPayment:', min_value=0.0, max_value=8.0, step=1.,format="%.2f")
        
        LP_CustomerPayments = st.number_input('LP_CustomerPayments:', min_value=-2.0, max_value=41000.0, step=1.,format="%.2f")
        LP_CollectionFees = st.number_input('LP_CollectionFees:', min_value=-95.0, max_value=25000.0, step=1.,format="%.2f")
        LP_GrossPrincipalLoss = st.number_input('LP_GrossPrincipalLoss:', min_value=-954.0, max_value=25000.0, step=1.,format="%.2f")
        LP_NetPrincipalLoss = st.number_input('LP_NetPrincipalLoss:', min_value=-2.0, max_value=41000.0, step=1.,format="%.2f")
        DateCreditPulled_Year = st.selectbox('DateCreditPulled_Year:',[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015])    
    
        button = st.form_submit_button('Predict')
       
    
    with open('scaler.pkl', 'rb') as f:  # open a model file
            scaler = pickle.load(f) # deserialize the list

    if button:

        data= np.array([DateCreditPulled, LoanOriginationQuarter, BorrowerAPR, BorrowerRate, EstimatedEffectiveYield,
                        EstimatedReturn, LoanMonthsSinceOrigination, MonthlyLoanPayment,LP_CustomerPayments,
                        LP_CollectionFees, LP_GrossPrincipalLoss, LP_NetPrincipalLoss, DateCreditPulled_Year]).reshape(1, -1)
        
        features = scaler.transform(data)
        
        with open(models[model_names[option]], 'rb') as f:  # open a model file
            model = pickle.load(f) # deserialize the list
         
        pred = get_prediction(data=features, model=model)
        st.success(prediction(model.predict(data)))
        st.write(f"The predicted LoanStatus is:  {pred}") 
        
#         model = models[model_names[option]]
          
            


if __name__ == '__main__':
    main()        
        
