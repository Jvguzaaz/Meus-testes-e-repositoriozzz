soma = 0

while True:
    soma1 = int(input("Digite um número (0 para sair): "))

    if soma1  == 0:
        break
    
    soma += soma1

    print(f"A soma atual é: {soma}")
print("Programa encerrado.")