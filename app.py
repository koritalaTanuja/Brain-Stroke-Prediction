import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("stroke_prediction_model.pkl", "rb"))

st.title("Stroke Prediction System")

st.write("Enter Patient Details")

gender = st.selectbox("Gender", [0,1])
age = st.number_input("Age")
hypertension = st.selectbox("Hypertension", [0,1])
heart_disease = st.selectbox("Heart Disease", [0,1])
avg_glucose_level = st.number_input("Average Glucose Level")
bmi = st.number_input("BMI")

if st.button("Predict"):

    input_data = np.array([[gender,
                            age,
                            hypertension,
                            heart_disease,
                            avg_glucose_level,
                            bmi]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("High Risk of Stroke")
    else:
        st.success("Low Risk of Stroke")