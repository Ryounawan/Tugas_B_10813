import streamlit as st
import pickle
import os

# Use os.path.join() to combine the directory and model file name
model_path = 'rf_diabetes_model.pkl'

# Check if the file exists in the specified directory
if os.path.exists(model_path):
    try:
        # Load the model from the pickle file
        with open(model_path, 'rb') as f:
            loaded_model = pickle.load(f)
        
        rf_model = loaded_model[0]
        
        # Streamlit App
        st.title("Prediksi Diabetes")

        st.write("Aplikasi ini digunakan untuk membantu memprediksi penyakit diabetes pada manusia")
        
        pregnancies = st.slider("Pregnancies", min_value=0, max_value=17, step=1)
        glucose = st.slider("Glucose (mg/dL)", min_value=0.0, max_value=199.0, step=0.1)
        bloodPressure = st.slider("Blood Pressure (mmHg)", min_value=0, max_value=122, step=2)
        skinThickness = st.slider("Skin Thickness (mm)", min_value=0, max_value=99, step=2)
        insulin = st.slider("Insulin (μU/mL)", min_value=0, max_value=846, step=10)
        bmi = st.slider("BMI", min_value=0.0, max_value=67.1, step=0.1)
        diabetesPedigreeFunction = st.slider("Diabetes Pedigree Function", min_value=0.07, max_value=2.42, step=0.1)
        age = st.slider("Age", min_value=21, max_value=81, step=1)
        
        # Predict diabetes based on input
        input_data = [[pregnancies, glucose, bloodPressure, skinThickness, insulin, bmi,
                       diabetesPedigreeFunction, age]]
        
        if st.button("Prediksi!"):
                rf_model_prediction = rf_model.predict(input_data)
                outcome_names = {0: 'Tidak Diabetes', 1: 'Diabetes'}
                st.write(f"Orang tersebut diprediksi **{outcome_names[rf_model_prediction[0]]}** oleh RF")
    except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")
else:
    st.error("File 'rf_diabetes_model.pkl' tidak ditemukan di direktori")
