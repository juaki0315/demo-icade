"""La interfaz: una página web hecha con Gradio que usa el modelo.

Arrancar en local:  python interfaz.py   ->  http://localhost:7860
Es el archivo que ejecuta Hugging Face Spaces (ver app_file en README.md).
"""
import os

import gradio as gr
import joblib

from train import entrenar

try:
    import spaces              # solo existe en Hugging Face (ZeroGPU)
    zerogpu = spaces.GPU
except ImportError:
    zerogpu = lambda f: f      # en vuestro ordenador no hace nada

if not os.path.exists("model.joblib"):
    entrenar()
model = joblib.load("model.joblib")


@zerogpu
def predecir(antiguedad, gasto, llamadas):
    X = [[antiguedad, gasto, llamadas]]
    prob = model.predict_proba(X)[0][1]
    return f"{prob:.0%}"


demo = gr.Interface(
    fn=predecir,
    inputs=[
        gr.Number(label="Meses como cliente", value=14),
        gr.Number(label="Gasto mensual (€)", value=59.9),
        gr.Number(label="Llamadas a soporte", value=4),
    ],
    outputs=gr.Textbox(label="Probabilidad de baja"),
    title="¿Se irá este cliente?",
    submit_btn="Predecir",
    flagging_mode="never",
)

demo.launch()
