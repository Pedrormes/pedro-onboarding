from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Lista em memória
clientes = []

# Modelo de validação
class Cliente(BaseModel):
    nome: str
    email: str
    cidade: str

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/clientes")
def listar_clientes():
    return {"clientes": clientes}

@app.post("/clientes", status_code=201)
def criar_cliente(cliente: Cliente):
    clientes.append(cliente)
    return cliente
