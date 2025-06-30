import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("pass_predictor_model.pkl")

st.set_page_config(page_title="Student Pass Prediction", page_icon="🎓")
st.title("🎓 Student Pass Prediction App")
st.write("Enter student data to check if they will pass or fail.")

# Input fields
study = st.number_input("📘 Study Hours", min_value=0.0, max_value=12.0, step=0.5)
attendance = st.number_input("📝 Attendance (%)", min_value=0.0, max_value=100.0, step=1.0)
sleep = st.number_input("🥱 Sleep Hours", min_value=0.0, max_value=12.0, step=0.5)
breaks = st.number_input("🕶️ Breaks Taken", min_value=0, max_value=10, step=1)

# Predict button
if st.button("Predict"):
    input_data = pd.DataFrame([[study, sleep, breaks, attendance]],
                              columns=['Study_hour', 'sleep_hour', 'Breaks', 'Attendance'])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ The student is likely to PASS!")
    else:
        st.error("❌ The student is likely to FAIL.")
