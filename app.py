import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('linear_regression_model.pkl', 'rb'))

st.title("📊 Sales Prediction App (Linear Regression)")
st.write("Predict sales using TV, Radio, and Newspaper budget")

tv = st.text_input("Enter TV sales...")
radio = st.text_input("Enter radio sales....")
newspaper = st.text_input("Enter newspaper sales.....")

if st.button("predict"):
    try:
        features = np.array([[float(tv), float(radio), float(newspaper)]])
        results = model.predict(features)
        st.write("Predicted sale::::", results[0])
    except:
        st.error("Please enter valid numeric values")
