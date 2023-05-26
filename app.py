import streamlit as st
import pickle
import sklearn

model = pickle.load(open('model.pkl', 'rb'))

st.title("Bank Churn Predictor")

age = st.number_input("Age")
credit_score = st.number_input("Credit Score")
tenure = st.number_input("Tenure")
balance = st.number_input("Balance")
hcc = st.selectbox("Has A Credit Card", ("Yes", "No"))
estimated_salary = st.number_input("Estimated Salary")

if hcc == "Yes":
    hcc = 0
else:
    hcc = 1

data = [[age, credit_score, tenure, balance, hcc, estimated_salary]]

if st.button("Predict"):
    prediction = model.predict(data)
    if prediction == 0:
        prediction = "No"
    else:
        prediction = "Yes"
    st.title(prediction)
