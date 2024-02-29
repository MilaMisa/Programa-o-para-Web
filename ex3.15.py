def numero_perfeito(numero):
    soma = 0
    for i in range(1, numero):
        if numero % i == 0:
            soma += i
    return soma == numero

numero= int(input("Digite um número: "))

if numero_perfeito(numero):
    print(f"O número {numero} é um número perfeito.")
else:
    print(f"O número {numero} não é um número perfeito.")
