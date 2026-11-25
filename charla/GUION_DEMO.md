# Guion de la demo en directo

En la demo se clona este repositorio, se ejecuta la app en local, se hace un cambio en una rama, se sube a GitHub y se ve publicado en internet.

- Repositorio: https://github.com/juaki0315/demo-icade
- Presentación: [Del_notebook_a_produccion.pptx](Del_notebook_a_produccion.pptx)

> En este guion, `TU-USUARIO-HF` es tu usuario de Hugging Face. Cámbialo también en `.github/workflows/deploy.yml`.

## Dónde se publica y por qué

| Opción | Por qué sí o por qué no |
|---|---|
| GitHub Pages | Solo sirve webs estáticas y no ejecuta Python. No nos sirve. |
| Hugging Face, Space de Docker | Pide el plan PRO. |
| **Hugging Face, Space de Gradio con hardware ZeroGPU** | **Gratis para cuentas personales (hasta 2 Spaces). Es el que usamos.** |

Por eso la interfaz está hecha con **Gradio** (`interfaz.py`). La API con FastAPI (`app.py`) se enseña en local, como la puerta para otros programas.

```
GitHub (código)  --merge en main-->  GitHub Actions  -->  Space de Gradio  -->  URL pública
```

La carpeta `charla/` (la presentación y este guion) no se sube al Space: el workflow solo copia la app.

---

## 1. Preparación (una sola vez, el día antes)

### 1.1 Git en la terminal
La demo usa comandos de `git`. GitHub Desktop no basta para eso.
1. Instala Git desde https://git-scm.com/download/win con las opciones por defecto.
2. Abre una terminal nueva y configúralo:

```powershell
git --version
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email@ejemplo.com"
```

### 1.2 Subir la primera versión a GitHub
Con GitHub Desktop:
1. Escribe el mensaje "Primera versión de la app".
2. Pulsa **Commit to main** y después **Push origin**.

O con la terminal, dentro de la carpeta `demo-icade`:
```powershell
git add .
git commit -m "Primera versión de la app"
git push
```

### 1.3 Crear el Space en Hugging Face
1. En https://huggingface.co/new-space, rellena:
   - Space name: `demo-icade`
   - SDK: **Gradio**, plantilla Blank
   - Hardware: **ZeroGPU**, la opción gratuita para cuentas personales
   - Visibilidad: Public
2. En https://huggingface.co/settings/tokens, crea un token de tipo **Write** y cópialo.

El bloque de configuración del `README.md` ya indica a Hugging Face que es una app de Gradio que se arranca con `interfaz.py`.

### 1.4 Conectar GitHub con Hugging Face
1. En https://github.com/juaki0315/demo-icade, ve a Settings → Secrets and variables → Actions → **New repository secret**.
2. Crea el secreto:
   - Nombre: `HF_TOKEN`
   - Valor: el token del paso anterior
3. En `.github/workflows/deploy.yml`, cambia `tu-usuario-hf` por tu usuario de Hugging Face.
4. Haz commit y push del cambio.
5. Comprueba el despliegue:
   - En la pestaña **Actions** de GitHub debe aparecer "Desplegar en Hugging Face" en verde.
   - En el Space, el estado pasa de *Building* a *Running* en 1–3 minutos.
   - La app queda en `https://TU-USUARIO-HF-demo-icade.hf.space`.

Mientras no exista el secreto `HF_TOKEN`, el workflow termina en verde sin desplegar nada.

### 1.5 Entorno listo y ensayo
Instalar las librerías tarda: hazlo antes y no en directo.

```powershell
python -m venv "$HOME\venv-charla"
& "$HOME\venv-charla\Scripts\Activate.ps1"
pip install -r requirements.txt
```

Haz la demo completa una vez. Para repetirla, quita el aviso de `interfaz.py` en `main` y haz push.

---

## 2. Checklist del día

- [ ] Internet comprobado.
- [ ] Sesión iniciada en GitHub y en Hugging Face en el navegador.
- [ ] Entorno `venv-charla` activado.
- [ ] El Space está en *Running*. Ábrelo 10 minutos antes: los Spaces gratuitos se duermen si nadie los usa.
- [ ] Una carpeta vacía para clonar en directo, por ejemplo `C:\demo`.
- [ ] Tres pestañas abiertas:
  - GitHub (repo)
  - GitHub (Actions)
  - el Space
- [ ] Letra de la terminal grande.
- [ ] Plan B: un vídeo grabado del despliegue.

---

## 3. La demo en directo (unos 20 minutos)

### Demo 1 · Clonar el repositorio (2 min)
```powershell
cd C:\demo
git clone https://github.com/juaki0315/demo-icade.git
cd demo-icade
code .
```
> «Clonar es descargar el proyecto entero, con todo su historial. Cada archivo es una pieza de la app.»

### Demo 2 · Entrenar el modelo (1 min)
```powershell
python train.py
```
Sale `accuracy = 0.86` y `Modelo guardado en model.joblib`.

### Demo 3 · La API y su página de prueba (3 min)
En la **terminal 1**:
```powershell
uvicorn app:app --reload
```
1. Abre http://localhost:8000/docs.
2. Ve a POST /predict → *Try it out*.
3. Pega este JSON y pulsa *Execute*:
```json
{"antiguedad": 14, "gasto": 59.9, "llamadas": 4}
```
4. La respuesta es `{"prob_churn": 0.681}`.

> «Esta es la puerta para otros programas: Excel, Power BI, otra app…»

### Demo 4 · La interfaz con Gradio (2 min)
En la **terminal 2**, con el entorno activado:
```powershell
python interfaz.py
```
1. Abre http://localhost:7860.
2. Pulsa **Predecir**. Sale **68%**.
3. Enseña el enlace **Use via API** al pie: Gradio también crea una API sola.

> «Está en localhost: solo funciona en mi portátil.»

### Demo 5 · Un cambio en una rama (4 min)
```powershell
git switch -c riesgo-alto
```
En `interfaz.py`, dentro de `predecir`, añade las dos líneas marcadas con `+` justo antes del `return` final:
```python
    prob = model.predict_proba(X)[0][1]
+   if prob > 0.5:
+       return f"{prob:.0%} · Riesgo alto: llamad esta semana"
    return f"{prob:.0%}"
```
1. Guarda el archivo.
2. En la terminal 2, para la app con **Ctrl+C** y vuelve a lanzarla con `python interfaz.py`.
3. Recarga el navegador y pulsa **Predecir**. Sale «68% · Riesgo alto: llamad esta semana».

Después enseña los cambios:
```powershell
git status
git diff
```

### Demo 6 · Commit y push (2 min)
```powershell
git add interfaz.py
git commit -m "Aviso de riesgo alto"
git push -u origin riesgo-alto
```

### Demo 7 · Pull request y merge (3 min)
1. En GitHub, pulsa **Compare & pull request**.
2. Enseña la pestaña *Files changed*.
3. Pulsa **Create pull request** y después **Merge pull request**.

### Demo 8 · Verlo publicado (2–3 min)
1. En la pestaña **Actions**, enseña el workflow en verde (unos 20 segundos).
2. En el Space, el estado pasa a *Building*. Mientras arranca, explica la diapositiva de Docker.
3. Cuando esté en *Running*, abre `https://TU-USUARIO-HF-demo-icade.hf.space` y pulsa **Predecir**. Aparece el aviso.

---

## 4. Si algo falla

| Problema | Qué hacer |
|---|---|
| No hay internet | Las demos 1 a 5 funcionan en local con el repo ya clonado. Pon el vídeo para las demos 6 a 8. |
| El Space tarda | Sigue con las diapositivas de Docker y AWS y vuelve después. |
| `python interfaz.py` dice que el puerto 7860 está ocupado | Hay otra copia de la app abierta: ciérrala con Ctrl+C. |
| `git push` pide credenciales | Inicia sesión en la ventana del navegador que se abre. |
| El Action falla en rojo | Revisa el secreto `HF_TOKEN` y el valor de `HF_SPACE` en `deploy.yml`. |
| El Space da error con ZeroGPU | Mira los *Logs* del Space. Comprueba que el hardware elegido es ZeroGPU y que el SDK es Gradio. |
