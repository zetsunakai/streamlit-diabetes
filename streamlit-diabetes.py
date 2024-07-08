import pickle
import streamlit as st

#membaca model
diabetes_model = pickle.load(open('diabetes_model_2.sav', 'rb'))

#judul web
st.title('Aplikasi Prediksi Diabetes')

col1, col2 = st.columns(2)

#form input
with col1 :
    Pregnancies = st.text_input ('Input nilai Kehamilan')
with col1 :
    Glucose = st.text_input ('Input nilai Gula darah')
with col1 :
    BloodPressure = st.text_input('Input nilai Tekanan Darah')
with col1 :
    SkinThickness = st.text_input('Input nilai Ketebalan Kulit')
with col2 :
    Insulin = st.text_input('Input nilai Insulin')
with col2 :
    BMI = st.text_input('Input nilai Indeks Massa Tubuh')
with col2 :
    DiabetesPedigreeFunction = st.text_input('Input nilai Function Diabetes')
with col2 :
    Age = st.text_input('Input nilai Umur')

#function prediksi
diab_diagnosis = ''

#button prediksi
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if (diab_prediction[0] == 1):
        diab_diagnosis = 'Pasien terkena Diabetes'
    else :
        diab_diagnosis = 'Pasien tidak terkena Diabetes'

    st.success(diab_diagnosis)