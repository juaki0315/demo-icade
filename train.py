"""Entrena un modelo de churn con datos sintéticos y lo guarda en model.joblib.

Es el equivalente a lo que haríais en vuestro notebook: entrenar una vez y guardar.
Ejecutar:  python train.py
"""
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def entrenar():
    rng = np.random.default_rng(42)
    n = 5000
    antiguedad = rng.integers(1, 121, n)        # meses como cliente
    gasto = rng.uniform(10, 150, n).round(2)     # gasto mensual (€)
    llamadas = rng.poisson(2, n)                 # llamadas a soporte

    # Riesgo de baja: más llamadas y más gasto lo suben; más antigüedad lo baja
    logit = -1.5 - 0.06 * antiguedad + 0.02 * gasto + 0.6 * llamadas
    churn = rng.random(n) < 1 / (1 + np.exp(-logit))

    X = np.column_stack([antiguedad, gasto, llamadas])
    X_train, X_test, y_train, y_test = train_test_split(X, churn, random_state=42)

    model = RandomForestClassifier(n_estimators=200, max_depth=6, random_state=42)
    model.fit(X_train, y_train)
    print(f"accuracy = {model.score(X_test, y_test):.2f}")

    joblib.dump(model, "model.joblib")
    print("Modelo guardado en model.joblib")


if __name__ == "__main__":
    entrenar()
