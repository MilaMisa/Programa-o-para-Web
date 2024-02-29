numero = int(input("Digite um número:"))
print(f"Tabuada de {numero}:")
for i in range(1, 11):
    multiplicacao = numero * i
    print(f"{numero}x{i} = {multiplicacao}")