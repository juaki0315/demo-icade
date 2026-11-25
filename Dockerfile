# Receta para empaquetar la app. Hugging Face Spaces la usa para construirla y publicarla.

# 1. Partir de un Python limpio (Hugging Face ejecuta la app con el usuario 1000)
FROM python:3.11-slim
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"
WORKDIR /app

# 2. Instalar las librerías
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copiar el código y entrenar el modelo (así no hay que subir archivos binarios)
COPY --chown=user . .
RUN python train.py

# 4. Arrancar la API (puerto 8000, interno) y la interfaz (puerto 8501, el público)
EXPOSE 8501
CMD uvicorn app:app --host 0.0.0.0 --port 8000 & \
    streamlit run interfaz.py --server.port 8501 --server.address 0.0.0.0
