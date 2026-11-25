---
title: App Churn
emoji: 📉
colorFrom: indigo
colorTo: blue
sdk: docker
app_port: 8501
---

# ¿Se irá este cliente?

App de ejemplo de la charla **Del notebook a producción: dar vida a un modelo de IA**.
Un modelo de churn, una API con FastAPI y una interfaz con Streamlit.

| Archivo | Pieza |
|---|---|
| `train.py` | El modelo: entrena y guarda `model.joblib` |
| `app.py` | La API (backend) con FastAPI |
| `interfaz.py` | La interfaz (frontend) con Streamlit |
| `requirements.txt` | Las librerías que necesita |
| `Dockerfile` | La receta para empaquetarla y publicarla |
| `.github/workflows/deploy.yml` | Publica en Hugging Face en cada cambio de `main` |

## Ejecutarla en vuestro ordenador

```bash
git clone https://github.com/juaki0315/demo-icade.git
cd demo-icade
pip install -r requirements.txt
python train.py
```

Después, en dos terminales:

```bash
uvicorn app:app --reload          # la API: http://localhost:8000/docs
streamlit run interfaz.py         # la app: http://localhost:8501
```

El bloque de arriba (entre `---`) es la configuración que lee Hugging Face Spaces.

La carpeta `charla/` tiene la presentación y el guion de la demo. No se publica en el Space: el workflow solo copia la app.
