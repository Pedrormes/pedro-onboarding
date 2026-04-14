import json

try:
    with open("clientes.json", "r", encoding="utf-8") as arquivo:
        clientes = json.load(arquivo)

    for cliente in clientes:
        print(f"Nome: {cliente['nome']}")
        print(f"Email: {cliente['email']}")
        print(f"Cidade: {cliente['cidade']}")
        print("-" * 30)

except FileNotFoundError:
    print("Erro: arquivo clientes.json não encontrado.")
