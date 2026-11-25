"""La interfaz: una página web que pide los datos y llama a la API.

Arrancar en local:  streamlit run interfaz.py
"""
import requests
import streamlit as st

URL_API = "http://localhost:8000/predict"

st.title("¿Se irá este cliente?")
antiguedad = st.number_input("Meses como cliente", 0, 120, 14)
gasto = st.number_input("Gasto mensual (€)", 0.0, 500.0, 59.9)
llamadas = st.number_input("Llamadas a soporte", 0, 20, 4)

if st.button("Predecir"):
    datos = {"antiguedad": antiguedad, "gasto": gasto, "llamadas": llamadas}
    r = requests.post(URL_API, json=datos)
    prob = r.json()["prob_churn"]
    st.metric("Probabilidad de baja", f"{prob:.0%}")
