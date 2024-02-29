lista = [int(x) for x in input("Digite uma lista de números (Separe por espaço): ").split()]
numeros_pares = list(filter(lambda x: x % 2 == 0, lista))
print("Números pares:", numeros_pares)
