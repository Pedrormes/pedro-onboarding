def gerar_impares():
    return [2 * i + 1 for i in range(10)]



if __name__ == "__main__":
    for numero in gerar_impares():
        print(numero)
