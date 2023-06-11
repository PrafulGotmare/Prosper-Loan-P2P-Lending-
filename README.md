# Prosper Loan Defaulter P2P Lending 

## Problem statement 

The problem statement chosen for this project is to predict a lending platform connecting borrowers with investors, wants to improve their loan approval process and minimize the risk of loan defaults. They aim to develop a machine learning model that can accurately predict whether a borrower is likely to default on their loan.

The project's objective is to create a predictive model that can assess the creditworthiness of loan applicants and provide insights into the probability of default. By identifying potential defaulters in advance, Prosper can take appropriate measures to mitigate risks and make informed decisions regarding loan approvals, interest rates, and credit limits.

Ultimately, the Prosper Loan Defaulter Prediction project aims to assist Prosper in making data-driven decisions to minimize loan defaults, reduce financial risks, attract more investors, and maintain a healthy lending marketplace.

## Business Problem Overview

In the context of the Prosper Loan Defaulter Prediction project, the main business problem revolves around assessing the risk of loan default for borrowers. Prosper is a lending platform that connects borrowers with investors, and ensuring the profitability and sustainability of the lending business requires identifying potential defaulters accurately.

The primary goal of this project is to develop a machine learning model that can predict whether a borrower is likely to default on their loan. By predicting loan defaulters in advance, Prosper can take proactive measures to mitigate risks, such as adjusting interest rates, setting appropriate credit limits, or even rejecting loan applications that have a high likelihood of default.

To address this business problem, the project will involve collecting historical Prosper loan data, performing data preprocessing & feature engineering, training machine learning models using appropriate algorithms, and evaluating their performance. The developed model will then be deployed into production to provide real-time predictions on new loan applications, enabling Prosper to make data-driven decisions and manage lending risks effectively.

By leveraging machine learning techniques to predict loan defaulters, Prosper aims to optimize its lending operations, minimize financial risks, and maintain a healthy and sustainable lending marketplace.

## Data Dictionary

This data set contains 113,937 loans with 81 variables on each loan, including loan amount, borrower rate , current loan status, borrower income, LoanStatus and many others.

## Project Pipeline

- **Data Understanding:** Here, we need to load the data and understand all features present in it. This would help us choose the right features that we will need for final model.
- **Data Cleaning:** In this step, The dataset containing information on 113,937 Rows with 81 Features requires data cleaning. In this project we used data cleaning process that involves identifying and handling missing values, Outlier detection, Encoding categorical variables, Standardizing variables, ensuring consistency in data formats, and resolving any inconsistencies or errors. The goal is to prepare a clean and reliable dataset for subsequent analysis and model development. This step is crucial to ensure accurate predictions and reliable insights for identifying potential loan defaulters.
- **Exploratory data analytics (EDA):** In this step, I need to perform univariate and bivariate analyses and Multivariate Analysis of the data, followed by feature transformations. For the current data set,However, i am can checking if there is any skewness in the data and try to mitigate it, as it might cause problems during the model-building phase. and also i am checking & visualizing of what are the factors that are affect a loan outcome status.
- **Train/Test Split:** Next i am performing in order to check the performance of our models. the dataset will undergo a train-test split to evaluate and validate the machine learning models effectively. 
In this Project the train-test split is typically performed randomly, ensuring that the distribution of loan default status is maintained in both subsets. A common split ratio is to allocate around 80% of the data to the training set and the remaining 20% to the testing set. However, the specific split ratio can vary depending on the dataset size and other considerations.
- **Model-Building/Hyperparameter Tuning:** This is the final step at which we can try different models and fine-tune their hyperparameters until we get the desired level of performance on the given dataset. For model building we used supervised learning algorithms such as: Logistic regression, Naives Bayes, Decision Tree, KNN, SVM, Random Forrest.
in order to test model accuracy i have used algorithms and check their accracy, Precsion, F1-Score.
- **Model Evaluation:** The goal is to select the best-performing model that can accurately classify borrowers as either defaulters or non-defaulters. so this are the steps that  involves the following Project :
      1.Splitting the dataset
      2.Performance metrics
      3.Cross-validation
      4.Hyperparameter tuning
      5.Comparing models algorithms
      6.Business requirements
By thoroughly evaluating the models, selecting the most accurate and reliable one, and considering business requirements, the Prosper Loan Defaulter Prediction project aims to deploy a robust and effective model that can predict loan defaulters with high precision and recall, thereby assisting in risk management and decision-making for loan approvals.
- **Project Deployment:** In the Prosper Loan Defaulter Prediction project, the deployment of the predictive model is achieved using Streamlit, a Python library for building interactive web applications. The purpose of deploying the model with Streamlit is to create a user-friendly interface that allows stakeholders to access and utilize the loan defaulter prediction functionality.
The application provides a interface where users can input relevant information about loan applicants, such as borrower attributes (ProsperScore, BorrowerAPR, CurrentDelinquencies, employment status, etc.). Upon submission of the form, the application sends the input data to the model for prediction. The Streamlit application then processes the input data and generates real-time predictions based on the trained model.
**Link** https://prosperloanprediction.streamlit.app/
