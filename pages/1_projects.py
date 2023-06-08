import streamlit as st
from PIL import Image
import pickle
import click

###################################################################




img1 = Image.open('prosper img.png')
img1 = img1.resize((440,180))
st.image(img1,use_column_width=False)
st.title("Prosper Loan Status Prediction using Machine Learning")
    
############
model = pickle.load(open('pages/Prosper_Loan.pkl', 'rb'))

############
def main():
    Term = st.selectbox('Term',(0,12,36,60))
    st.write("Term Selected : ", Term)
    
    CreditGrade = st.selectbox('CreditGrade',(0,1,2,3,4,5,6,7))
    st.write("CreditGrade Selected : ", CreditGrade)
    
    CurrentDelinquencies = st.number_input("CurrentDelinquencies",min_value=5.875166464356, max_value=5.875166464356)
    st.write("By default CurrentDelinquencies Selected : ", CurrentDelinquencies)
    
    BorrowerAPR = st.number_input('BorrowerAPR', min_value=0.00653,max_value=0.510685 )
    st.write("BorrowerAPR Selected : ", BorrowerAPR)
    
    BorrowerRate = st.number_input('BorrowerRate', min_value=0.0,max_value=0.47 )
    st.write("BorrowerRate Selected : ", BorrowerRate)
    
    BorrowerState = st.number_input('BorrowerState', min_value=0,max_value=50 )
    st.write("BorrowerState Selected : ", BorrowerState)
    
    DebtToIncomeRatio = st.number_input('DebtToIncomeRatio', min_value=0.0,max_value=10.01)
    st.write("DebtToIncomeRatio Selected : ", DebtToIncomeRatio)
    
#########    
    
    EstimatedEffectiveYield= st.number_input("EstimatedEffectiveYield", min_value= -0.1827,max_value=0.3199)
    st.write("EstimatedEffectiveYield Selected : ", EstimatedEffectiveYield)
    
    EstimatedLoss = st.number_input('EstimatedLoss', min_value=0.0049,max_value=0.366 )
    st.write("EstimatedLoss Selected : ", EstimatedLoss)
    
    EstimatedReturn = st.number_input('EstimatedReturn', min_value= -0.1827,max_value=0.2837 )
    st.write("EstimatedReturn Selected : ", EstimatedReturn)
    
    ProsperRating_numeric = st.number_input('ProsperRating (numeric)', min_value=1,max_value=7 )
    st.write("ProsperRating_numeric Selected : ", ProsperRating_numeric)
    
    ProsperRating_Alpha = st.number_input('ProsperRating (Alpha)', min_value=0,max_value=6)
    st.write("ProsperRating_Alpha Selected : ", ProsperRating_Alpha)
    
#########
    
    ProsperScore= st.number_input("ProsperScore", min_value=5.8737,max_value=6.0)
    st.write("ProsperScore Selected : ", ProsperScore)
    
    EmploymentStatus = st.number_input('EmploymentStatus', min_value=0,max_value=2 )
    st.write("EmploymentStatus Selected : ", EmploymentStatus)
    
    CreditScoreRangeLower = st.number_input('CreditScoreRangeLower', min_value=0,max_value=880 )
    st.write("CreditScoreRangeLower Selected : ", CreditScoreRangeLower)
    
    CreditScoreRangeUpper = st.number_input('CreditScoreRangeUpper', min_value=19,max_value=899 )
    st.write("CreditScoreRangeUpper Selected : ", CreditScoreRangeUpper)
    
    OpenCreditLines = st.number_input('OpenCreditLines', min_value=0,max_value=51)
    st.write("OpenCreditLines Selected : ", OpenCreditLines)
    
#########    
    
    TotalCreditLinespast7years= st.number_input("TotalCreditLinespast7years", min_value=2,max_value=136)
    st.write("TotalCreditLinespast7years Selected : ", TotalCreditLinespast7years)
    
    OpenRevolvingAccounts = st.number_input('OpenRevolvingAccounts', min_value=0,max_value=51 )
    st.write("OpenRevolvingAccounts Selected : ", OpenRevolvingAccounts)
    
    OpenRevolvingMonthlyPayment = st.number_input('OpenRevolvingMonthlyPayment', min_value=0,max_value=14985 )
    st.write("OpenRevolvingMonthlyPayment Selected : ", OpenRevolvingMonthlyPayment)
    
    TotalInquiries = st.number_input('TotalInquiries', min_value=0,max_value=379 )
    st.write("TotalInquiries Selected : ", TotalInquiries)
    
    RevolvingCreditBalance = st.number_input('RevolvingCreditBalance', min_value=0,max_value=879785)
    st.write("RevolvingCreditBalance Selected : ", RevolvingCreditBalance)

#########
    
    LoanOriginationDate= st.number_input("LoanOriginationDate", min_value=0,max_value=1855)
    st.write("LoanOriginationDate Selected : ", LoanOriginationDate)
    
    LP_CustomerPrincipalPayments = st.number_input('LP_CustomerPrincipalPayments', min_value=0,max_value=35000 )
    st.write("LP_CustomerPrincipalPayments Selected : ", LP_CustomerPrincipalPayments)
    
    LP_InterestandFees = st.number_input('LP_InterestandFees', min_value=0.0,max_value=13206.08 )
    st.write("LP_InterestandFees Selected : ", LP_InterestandFees)
    
    LP_NetPrincipalLoss = st.number_input('LP_NetPrincipalLoss', min_value=0,max_value=25000 )
    st.write("LP_NetPrincipalLoss Selected : ", LP_NetPrincipalLoss)
    
    LP_NonPrincipalRecoverypayments = st.number_input('LP_NonPrincipalRecoverypayments', min_value=0.0,max_value=21117.9)
    st.write("LP_NonPrincipalRecoverypayments Selected : ", LP_NonPrincipalRecoverypayments)
    
    InvestmentFromFriendsCount = st.number_input('InvestmentFromFriendsCount', min_value=0,max_value=33)
    st.write("InvestmentFromFriendsCount Selected : ", InvestmentFromFriendsCount)
    
    Investors = st.number_input('Investors', min_value=1,max_value=1189)
    st.write("Investors Selected : ", Investors)

#########
    # st.caption('If you want to save Filled info click here')
    # if st.button("Submit"):
    # st.info('Before Click predict button you must fill all inputs!', icon="ℹ️")  
      
    features = [['Term','CreditGrade','BorrowerAPR','BorrowerRate','BorrowerState','CurrentDelinquencies',
    'DebtToIncomeRatio','EstimatedEffectiveYield','EstimatedLoss','EstimatedReturn','ProsperRating (numeric)',
    'ProsperRating (Alpha)','ProsperScore','EmploymentStatus','CreditScoreRangeLower','CreditScoreRangeUpper',
    'OpenCreditLines', 'TotalCreditLinespast7years','OpenRevolvingAccounts','OpenRevolvingMonthlyPayment',
    'TotalInquiries','RevolvingCreditBalance','LoanOriginationDate',
    'LP_CustomerPrincipalPayments','LP_InterestandFees','LP_NetPrincipalLoss','LP_NonPrincipalRecoverypayments',
    'InvestmentFromFriendsCount','Investors']]
    print(features)
        
        
#################################################################################
        
    # Create a prediction button
    st.caption('Want to check Loan status Prediction Click here')
    if st.button('Predict'):
        
        # Prepare features for prediction
        
        features = [[Term,CreditGrade,BorrowerAPR,BorrowerRate,BorrowerState,CurrentDelinquencies,
    DebtToIncomeRatio,EstimatedEffectiveYield,EstimatedLoss,EstimatedReturn,ProsperRating_numeric,
    ProsperRating_Alpha,ProsperScore,EmploymentStatus,CreditScoreRangeLower,CreditScoreRangeUpper,
    OpenCreditLines, TotalCreditLinespast7years,OpenRevolvingAccounts,OpenRevolvingMonthlyPayment,
    TotalInquiries,RevolvingCreditBalance,LoanOriginationDate,
    LP_CustomerPrincipalPayments,LP_InterestandFees,LP_NetPrincipalLoss,LP_NonPrincipalRecoverypayments,
    InvestmentFromFriendsCount,Investors]]  # Modify this line based on your loan features
        

        # Make the prediction
        prediction = model.predict(features)
        

        # Map prediction to loan status label
        # loan_status = 'Default' if prediction == 1 else 'Not Default'
        # Define the function to predict the loan status
        
        def predict_loan_status(model, features):
            prediction = model.predict(features)
            if prediction == 1:
                return 'Loan is Defaulted'
            else:
                st.success('Prediction successful!', icon="✅")
                return 'The Loan is Not Defaulted'
    
        loan_status = predict_loan_status(model, features)
    
    
        # Display the prediction
        st.write('Loan Status Prediction:', loan_status)

if __name__ == '__main__':
    main()
