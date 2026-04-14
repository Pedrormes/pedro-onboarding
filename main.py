from fastapi import FastAPI
from impares import gerar_impares

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/impares")
def impares():
    return {"impares": gerar_impares()}
