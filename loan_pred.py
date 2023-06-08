import streamlit as st
from PIL import Image
import pickle
import click
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import json
import requests
import time
import streamlit_lottie
from streamlit_option_menu import option_menu
###################################################################

# Add icon

img = Image.open('Prosper logo.png') 

# config function
st.set_page_config(page_title='Prosper Loan' , page_icon=img)

###################################################################

# 1. as sidebar menu

with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Prosper Loan Project", "About Me"],  # required
                icons=["house", "book", "envelope"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
            # return selected

# selected = streamlit_menu(example=EXAMPLE_NO)

if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "Prosper Loan Projects":
    st.title(f"You have selected {selected}")
if selected == "About Me":
    st.title(f"You have selected {selected}")



###################################################################

st.lottie("https://assets2.lottiefiles.com/packages/lf20_qufi1zre.json")  

###################################################################

model = pickle.load(open('Prosper_Loan.pkl', 'rb'))

def main():
    img1 = Image.open('prosper img.png')
    img1 = img1.resize((440,180))
    st.image(img1,use_column_width=False)
    st.header("Prosper Loan Status Prediction using Machine Learning")
    
############
    
    



# -----------------------------------------------------------------------------------------------------------
    # ## For gender
    # gen_display = ('Female','Male')
    # gen_options = list(range(len(gen_display)))
    # gen = st.selectbox("Gender",gen_options, format_func=lambda x: gen_display[x])

    Term = st.sidebar.selectbox('Term',(0,12,36,60))
    st.sidebar.write("Term Selected : ", Term)
    
    CreditGrade = st.sidebar.selectbox('CreditGrade',(0,1,2,3,4,5,6,7))
    st.sidebar.write("CreditGrade Selected : ", CreditGrade)
    
    CurrentDelinquencies = st.sidebar.number_input("CurrentDelinquencies",min_value=5.875166464356, max_value=5.875166464356)
    st.sidebar.write("By default CurrentDelinquencies Selected : ", CurrentDelinquencies)
    
    BorrowerAPR = st.sidebar.number_input('BorrowerAPR', min_value=0.00653,max_value=0.510685 )
    st.sidebar.write("BorrowerAPR Selected : ", BorrowerAPR)
    
    BorrowerRate = st.sidebar.number_input('BorrowerRate', min_value=0.0,max_value=0.47 )
    st.sidebar.write("BorrowerRate Selected : ", BorrowerRate)
    
    BorrowerState = st.sidebar.number_input('BorrowerState', min_value=0,max_value=50 )
    st.sidebar.write("BorrowerState Selected : ", BorrowerState)
    
    DebtToIncomeRatio = st.sidebar.number_input('DebtToIncomeRatio', min_value=0.0,max_value=10.01)
    st.sidebar.write("DebtToIncomeRatio Selected : ", DebtToIncomeRatio)
    
#########    
    
    EstimatedEffectiveYield= st.sidebar.number_input("EstimatedEffectiveYield", min_value= -0.1827,max_value=0.3199)
    st.sidebar.write("EstimatedEffectiveYield Selected : ", EstimatedEffectiveYield)
    
    EstimatedLoss = st.sidebar.number_input('EstimatedLoss', min_value=0.0049,max_value=0.366 )
    st.sidebar.write("EstimatedLoss Selected : ", EstimatedLoss)
    
    EstimatedReturn = st.sidebar.number_input('EstimatedReturn', min_value= -0.1827,max_value=0.2837 )
    st.sidebar.write("EstimatedReturn Selected : ", EstimatedReturn)
    
    ProsperRating_numeric = st.sidebar.number_input('ProsperRating (numeric)', min_value=1,max_value=7 )
    st.sidebar.write("ProsperRating_numeric Selected : ", ProsperRating_numeric)
    
    ProsperRating_Alpha = st.sidebar.number_input('ProsperRating (Alpha)', min_value=0,max_value=6)
    st.sidebar.write("ProsperRating_Alpha Selected : ", ProsperRating_Alpha)
    
#########
    
    ProsperScore= st.sidebar.number_input("ProsperScore", min_value=5.8737,max_value=6.0)
    st.sidebar.write("ProsperScore Selected : ", ProsperScore)
    
    EmploymentStatus = st.sidebar.number_input('EmploymentStatus', min_value=0,max_value=2 )
    st.sidebar.write("EmploymentStatus Selected : ", EmploymentStatus)
    
    CreditScoreRangeLower = st.sidebar.number_input('CreditScoreRangeLower', min_value=0,max_value=880 )
    st.sidebar.write("CreditScoreRangeLower Selected : ", CreditScoreRangeLower)
    
    CreditScoreRangeUpper = st.sidebar.number_input('CreditScoreRangeUpper', min_value=19,max_value=899 )
    st.sidebar.write("CreditScoreRangeUpper Selected : ", CreditScoreRangeUpper)
    
    OpenCreditLines = st.sidebar.number_input('OpenCreditLines', min_value=0,max_value=51)
    st.sidebar.write("OpenCreditLines Selected : ", OpenCreditLines)
    
#########    
    
    TotalCreditLinespast7years= st.sidebar.number_input("TotalCreditLinespast7years", min_value=2,max_value=136)
    st.sidebar.write("TotalCreditLinespast7years Selected : ", TotalCreditLinespast7years)
    
    OpenRevolvingAccounts = st.sidebar.number_input('OpenRevolvingAccounts', min_value=0,max_value=51 )
    st.sidebar.write("OpenRevolvingAccounts Selected : ", OpenRevolvingAccounts)
    
    OpenRevolvingMonthlyPayment = st.sidebar.number_input('OpenRevolvingMonthlyPayment', min_value=0,max_value=14985 )
    st.sidebar.write("OpenRevolvingMonthlyPayment Selected : ", OpenRevolvingMonthlyPayment)
    
    TotalInquiries = st.sidebar.number_input('TotalInquiries', min_value=0,max_value=379 )
    st.sidebar.write("TotalInquiries Selected : ", TotalInquiries)
    
    RevolvingCreditBalance = st.sidebar.number_input('RevolvingCreditBalance', min_value=0,max_value=879785)
    st.sidebar.write("RevolvingCreditBalance Selected : ", RevolvingCreditBalance)

#########
    
    LoanOriginationDate= st.sidebar.number_input("LoanOriginationDate", min_value=0,max_value=1855)
    st.sidebar.write("LoanOriginationDate Selected : ", LoanOriginationDate)
    
    LP_CustomerPrincipalPayments = st.sidebar.number_input('LP_CustomerPrincipalPayments', min_value=0,max_value=35000 )
    st.sidebar.write("LP_CustomerPrincipalPayments Selected : ", LP_CustomerPrincipalPayments)
    
    LP_InterestandFees = st.sidebar.number_input('LP_InterestandFees', min_value=0.0,max_value=13206.08 )
    st.sidebar.write("LP_InterestandFees Selected : ", LP_InterestandFees)
    
    LP_NetPrincipalLoss = st.sidebar.number_input('LP_NetPrincipalLoss', min_value=0,max_value=25000 )
    st.sidebar.write("LP_NetPrincipalLoss Selected : ", LP_NetPrincipalLoss)
    
    LP_NonPrincipalRecoverypayments = st.sidebar.number_input('LP_NonPrincipalRecoverypayments', min_value=0.0,max_value=21117.9)
    st.sidebar.write("LP_NonPrincipalRecoverypayments Selected : ", LP_NonPrincipalRecoverypayments)
    
    InvestmentFromFriendsCount = st.sidebar.number_input('InvestmentFromFriendsCount', min_value=0,max_value=33)
    st.sidebar.write("InvestmentFromFriendsCount Selected : ", InvestmentFromFriendsCount)
    
    Investors = st.sidebar.number_input('Investors', min_value=1,max_value=1189)
    st.sidebar.write("Investors Selected : ", Investors)

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
















#------------------------------------------------------------------------------------------------------


###### dummy code
# import pickle
# import streamlit as st
 
# # loading the trained model
# pickle_in = open('Prosper_Loan.pkl', 'rb') 
# classifier = pickle.load(pickle_in)
 
# @st.cache()
  
# # defining the function which will make the prediction using the data which the user inputs 
# def prediction(Term,CreditGrade,ClosedDate,BorrowerAPR,BorrowerRate,BorrowerState,CurrentDelinquencies,
#     DebtToIncomeRatio,EstimatedEffectiveYield,EstimatedLoss,EstimatedReturn,ProsperRating_numeric,
#     ProsperRating_Alpha,ProsperScore,EmploymentStatus,CreditScoreRangeLower,CreditScoreRangeUpper,
#     OpenCreditLines, TotalCreditLinespast7years,OpenRevolvingAccounts,OpenRevolvingMonthlyPayment,
#     TotalInquiries,RevolvingCreditBalance,LoanOriginationDate,
#     LP_CustomerPrincipalPayments,LP_InterestandFees,LP_NetPrincipalLoss,LP_NonPrincipalRecoverypayments,
#     InvestmentFromFriendsCount):   
 
#     # Pre-processing user input    
#     if Term == "Male":
#         Gender = 0
#     else:
#         Gender = 1
 
#     if Married == "Unmarried":
#         Married = 0
#     else:
#         Married = 1
 
#     if Credit_History == "Unclear Debts":
#         Credit_History = 0
#     else:
#         Credit_History = 1  
 
#     LoanAmount = LoanAmount / 1000
 
#     # Making predictions 
#     prediction = classifier.predict( 
#         [[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])
     
#     if prediction == 0:
#         pred = 'Rejected'
#     else:
#         pred = 'Approved'
#     return pred
      
  
# # this is the main function in which we define our webpage  
# def main():       
#     # front end elements of the web page 
#     html_temp = """ 
#     <div style ="background-color:yellow;padding:13px"> 
#     <h1 style ="color:black;text-align:center;">Streamlit Loan Prediction ML App</h1> 
#     </div> 
#     """
      
#     # display the front end aspect
#     st.markdown(html_temp, unsafe_allow_html = True) 
      
#     # following lines create boxes in which user can enter data required to make prediction 
#     Gender = st.selectbox('Gender',("Male","Female"))
#     Married = st.selectbox('Marital Status',("Unmarried","Married")) 
#     ApplicantIncome = st.number_input("Applicants monthly income") 
#     LoanAmount = st.number_input("Total loan amount")
#     Credit_History = st.selectbox('Credit_History',("Unclear Debts","No Unclear Debts"))
#     result =""
      
#     # when 'Predict' is clicked, make the prediction and store it 
#     if st.button("Predict"): 
#         result = prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History) 
#         st.success('Your loan is {}'.format(result))
#         print(LoanAmount)
     
# if __name__=='__main__': 
#     main()




###################################################################

# video_file = open('Praful_loan_pred_Loan Defaulted.mp4', 'rb')
# video_bytes = video_file.read()

# st.video(video_bytes)


# video_file = open('Praful_loan_pred_Loan is Not Defaulted.mp4', 'rb')
# video_bytes = video_file.read()

# st.video(video_bytes)







hide_menu_style ="""
        <style>
        #MainMMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)        