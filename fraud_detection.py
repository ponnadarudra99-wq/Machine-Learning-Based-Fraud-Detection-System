import streamlit as st
import numpy as np
import pickle

st.title("Machine Learning-Based Fraud Detection System")

with open("fraud_detection_model.pkl", "rb") as file:
    model = pickle.load(file)

amount = st.number_input("Enter Transaction Amount")
transaction_type = st.selectbox("Select Transaction Type", [1, 2, 3, 4])
account_age = st.number_input("Enter Account Age (Months)")
is_international = st.selectbox("International Transaction?", [0, 1])
is_high_risk = st.selectbox("High Risk Transaction?", [0, 1])

if st.button("Predict Fraud Status"):
    data = np.array([[amount, transaction_type, account_age, is_international, is_high_risk]])
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("⚠️ Fraud Transaction Detected")
    else:
        st.success("✅ Normal Legitimate Transaction")