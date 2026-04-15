# Pedro Rodrigues Mesquita

data de início na Vortex:09-04-2026
Sou estudante de Sistemas de Informação na Faculdade Estadual de Montes Claros e atualmente atuo na Vortex. Tenho grande interesse na área de computação, com foco em desenvolvimento de software e na criação de soluções tecnológicas eficientes.
## Push pelo Cmd

\-  adicionar stack no README

# 🚀 API de Clientes

## 📌 Sobre

API desenvolvida com FastAPI para cadastro e listagem de clientes utilizando PostgreSQL.

---

## ⚙️ Requisitos

- Python 3.x
- PostgreSQL instalado e rodando

---

## 📦 Instalação

Clone o repositório:

git clone https://github.com/Pedrormes/pedro-onboarding.git

Entre na pasta:

cd pedro-onboarding

Instale dependências:

pip install fastapi uvicorn psycopg2-binary

---

## 🗄️ Banco de dados

Criar banco:

CREATE DATABASE clientes_db;

Conectar:

\c clientes_db

Criar tabela:

CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    cidade TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

---

## 🔐 Variável de ambiente

No Windows:

set DATABASE_URL=postgresql://postgres:SUA_SENHA@localhost:5432/clientes_db

---

## ▶️ Como rodar

python -m uvicorn main:app --reload

---

## 🌐 Endpoints

### GET /

Retorna status da API

---

### GET /clientes

Lista todos os clientes

---

### POST /clientes

Cria um cliente

---

## 🧪 Exemplos

### Criar cliente (POST)

curl -X POST http://localhost:8000/clientes ^
-H "Content-Type: application/json" ^
-d "{\"nome\":\"Pedro\",\"email\":\"pedro@email.com\",\"cidade\":\"Montes Claros\"}"

---

### Listar clientes (GET)

curl http://localhost:8000/clientes