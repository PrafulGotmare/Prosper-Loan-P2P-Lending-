
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import pickle

models = {'logistic_model':'logistic_model.pkl', 
#           'classifier_regressor': 'classifier_regressor.pkl', 
          'gnaivebayes': 'gnaivebayes.pkl', 
          'knn_clf': 'knn_clf.pkl',
          'dtree_clf' : 'dtree_clf.pkl', 
           
#           'svc_model': 'svc_model.pkl', 
          'rforest_clf': 'rforest_clf.pkl', 
          'adaboost': 'adaboost.pkl'}


# for key, mod in models.items():
#     with open(mod, 'rb') as f:  # open a model file
#         pickle.load(mod, f) # deserialize the list

pickle_in = open('adaboost.pkl', 'rb') 
adaboost_model = pickle.load(pickle_in)

pickle_in = open('logistic_model.pkl', 'rb') 
LG_model = pickle.load(pickle_in)

pickle_in = open('dtree_clf.pkl', 'rb') 
DT_model = pickle.load(pickle_in)

pickle_in = open('knn_clf.pkl', 'rb') 
KNN_model = pickle.load(pickle_in)

pickle_in = open('svc_model.pkl', 'rb') 
SVC_model = pickle.load(pickle_in)

pickle_in = open('rforest_clf.pkl', 'rb') 
RF_model = pickle.load(pickle_in)

pickle_in = open('gnaivebayes.pkl', 'rb') 
NB_model = pickle.load(pickle_in)




not_default_example = {'DateCreditPulled': 14346,
 'LoanOriginationQuarter': 17,
 'BorrowerAPR': 0.16516,
 'BorrowerRate': 0.158,
 'EstimatedEffectiveYield': 0.1787990044912847,
 'EstimatedReturn': 0.1077559341514328,
 'LoanMonthsSinceOrigination': 78,
 'MonthlyLoanPayment': 5.803416625940581,
 'LP_CustomerPayments': 11396.14,
 'LP_CollectionFees': 0.0,
 'LP_GrossPrincipalLoss': 0.0,
 'LP_NetPrincipalLoss': 0.0,
 'DateCreditPulled_Year': 2007}


default_example = {'DateCreditPulled': 47155,
 'LoanOriginationQuarter': 14,
 'BorrowerAPR': 0.35797,
 'BorrowerRate': 0.3177,
 'EstimatedEffectiveYield': 0.2896,
 'EstimatedReturn': 0.1246,
 'LoanMonthsSinceOrigination': 23,
 'MonthlyLoanPayment': 5.163127456486353,
 'LP_CustomerPayments': 521.13,
 'LP_CollectionFees': 0.0,
 'LP_GrossPrincipalLoss': 3790.25,
 'LP_NetPrincipalLoss': 3790.25,
 'DateCreditPulled_Year': 2012}






def get_prediction(data,model):
    """
    Predict the class of a given data point.
    """
    return model.predict(data)
