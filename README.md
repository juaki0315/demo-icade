---
title: ¿Se irá este cliente?
emoji: 📉
colorFrom: indigo
colorTo: blue
sdk: gradio
sdk_version: 6.32.0
app_file: interfaz.py
pinned: false
---

# ¿Se irá este cliente?

App de ejemplo de la charla **Del notebook a producción: dar vida a un modelo de IA**.
Un modelo de churn, una interfaz con Gradio para las personas y una API con FastAPI para otros programas.

| Archivo | Pieza |
|---|---|
| `train.py` | El modelo: entrena y guarda `model.joblib` |
| `interfaz.py` | La interfaz (Gradio): la web para las personas. Es lo que se publica |
| `app.py` | La API (FastAPI): la puerta para otros programas |
| `requirements.txt` | Las librerías que necesita |
| `.github/workflows/deploy.yml` | Publica en Hugging Face en cada cambio de `main` |

## Ejecutarla en vuestro ordenador

```bash
git clone https://github.com/juaki0315/demo-icade.git
cd demo-icade
pip install -r requirements.txt
python train.py
```

La interfaz:

```bash
python interfaz.py                # http://localhost:7860
```

La API, en otra terminal:

```bash
uvicorn app:app --reload          # http://localhost:8000/docs
```

## Publicarla

El bloque de arriba (entre `---`) es la configuración que lee Hugging Face Spaces: un Space de Gradio que ejecuta `interfaz.py`.
Con una cuenta gratuita, el Space debe usar el hardware **ZeroGPU**.

La carpeta `charla/` tiene la presentación y el guion de la demo. No se publica en el Space: el workflow solo copia la app.
