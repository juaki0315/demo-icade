"""La API: recibe los datos de un cliente y devuelve la probabilidad de baja.

Es la puerta para otros programas (Excel, Power BI, otra app, un asistente de IA…).
Las personas usan la interfaz (interfaz.py).

Arrancar en local:  uvicorn app:app --reload
Probarla:           http://localhost:8000/docs
"""
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="API de churn")           # (1) la API, «el camarero»
model = joblib.load("model.joblib")           # (2) cargar el modelo una sola vez


class Cliente(BaseModel):                     # (3) qué datos esperamos
    antiguedad: int
    gasto: float
    llamadas: int


@app.post("/predict")                         # (4) el endpoint
def predict(c: Cliente):
    X = [[c.antiguedad, c.gasto, c.llamadas]]
    prob = model.predict_proba(X)[0][1]
    return {"prob_churn": round(float(prob), 3)}
