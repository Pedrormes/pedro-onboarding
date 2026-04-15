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


