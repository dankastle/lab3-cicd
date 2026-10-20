import os
from flask import Flask

app = Flask(__name__)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/parcela")
def parcela():
    return{
        "nombre": os.getenv("PARCELA_NOMBRE", "sin-nombre"),
        "umbral_humedad": int(os.getenv("UMBRAL_HUMEDAD", "30")),
    }

@app.get("/alerta")
def alerta():
    humedad = 22
    umbral = int(os.getenv("UMBRAL_HUMEDAD", "30"))
    return {
        "humedad": humedad, 
        "alerta": humedad < umbral, 
    }
