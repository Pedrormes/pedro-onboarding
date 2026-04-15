from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import os

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")

# conexão
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

class Cliente(BaseModel):
    nome: str
    email: str
    cidade: str

@app.get("/")
def home():
    return {"status": "ok"}

@app.post("/clientes", status_code=201)
def criar_cliente(cliente: Cliente):
    cursor.execute(
        "INSERT INTO clientes (nome, email, cidade) VALUES (%s, %s, %s) RETURNING id, nome, email, cidade",
        (cliente.nome, cliente.email, cliente.cidade)
    )
    novo_cliente = cursor.fetchone()
    conn.commit()

    return {
        "id": novo_cliente[0],
        "nome": novo_cliente[1],
        "email": novo_cliente[2],
        "cidade": novo_cliente[3]
    }

@app.get("/clientes")
def listar_clientes():
    cursor.execute("SELECT id, nome, email, cidade FROM clientes")
    dados = cursor.fetchall()

    clientes = []
    for c in dados:
        clientes.append({
            "id": c[0],
            "nome": c[1],
            "email": c[2],
            "cidade": c[3]
        })

    return {"clientes": clientes}