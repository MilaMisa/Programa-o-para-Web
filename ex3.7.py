soma = 0
numero = float(input("Digite um número:"))
contador = 0
while numero >= 0:
    soma += numero
    numero = float(input("Digite mais um número (Digite um número negativo para parar:"))
    contador +=1
media = soma / contador
print(f"A média dos números digitados é {media}")
