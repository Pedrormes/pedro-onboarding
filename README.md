# Pedro Rodrigues Mesquita

data de início na Vortex:09-04-2026
Sou estudante de Sistemas de Informação na Faculdade Estadual de Montes Claros e atualmente atuo na Vortex. Tenho grande interesse na área de computação, com foco em desenvolvimento de software e na criação de soluções tecnológicas eficientes.
## Push pelo Cmd

\-  adicionar stack no README

## Como rodar a API

Instalar dependências:
pip install fastapi uvicorn

Rodar:
uvicorn main:app --reload

Acessar:
http://localhost:8000

## Testando a API

### Criar cliente

curl -X POST http://localhost:8000/clientes ^
-H "Content-Type: application/json" ^
-d "{\"nome\":\"Pedro\",\"email\":\"pedro@email.com\",\"cidade\":\"Montes Claros\"}"

### Listar clientes

GET http://localhost:8000/clientes

##  Como rodar o projeto

### 1. Instalar dependências

pip install fastapi uvicorn psycopg2-binary

---

### 2. Instalar e rodar o PostgreSQL

Instale o PostgreSQL e certifique-se que está rodando localmente.

---

### 3. Criar banco de dados

Abra o SQL Shell (psql) e execute:

CREATE DATABASE clientes_db;

---

### 4. Criar tabela

Conecte no banco:

\c clientes_db

Execute:

CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    cidade TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

---

### 5. Configurar variável de ambiente

No Windows (CMD):

set DATABASE_URL=postgresql://postgres:SUA_SENHA@localhost:5432/clientes_db

---

### 6. Rodar a API

python -m uvicorn main:app --reload

---

### 7. Testar a API

Abra no navegador:

http://localhost:8000/docs

---

###  Endpoints

GET /clientes → lista clientes  
POST /clientes → cria cliente  

Exemplo de JSON para POST:

{
  "nome": "Pedro",
  "email": "pedro@email.com",
  "cidade": "Montes Claros"
}

