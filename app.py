import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("stroke_prediction_model.pkl")

st.title("Brain Stroke Prediction")

st.write("Enter Patient Details")

gender = st.selectbox("Gender", [0,1])
age = st.number_input("Age", 0, 120, 30)
hypertension = st.selectbox("Hypertension", [0,1])
heart_disease = st.selectbox("Heart Disease", [0,1])
ever_married = st.selectbox("Ever Married", [0,1])
work_type = st.selectbox("Work Type", [0,1,2,3,4])
Residence_type = st.selectbox("Residence Type", [0,1])
avg_glucose_level = st.number_input("Average Glucose Level")
bmi = st.number_input("BMI")
smoking_status = st.selectbox("Smoking Status", [0,1,2,3])

if st.button("Predict"):

    data = pd.DataFrame([[gender,
                          age,
                          hypertension,
                          heart_disease,
                          ever_married,
                          work_type,
                          Residence_type,
                          avg_glucose_level,
                          bmi,
                          smoking_status]],
                        columns=[
                            "gender",
                            "age",
                            "hypertension",
                            "heart_disease",
                            "ever_married",
                            "work_type",
                            "Residence_type",
                            "avg_glucose_level",
                            "bmi",
                            "smoking_status"
                        ])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("High Risk of Stroke")
    else:
        st.success("Low Risk of Stroke")