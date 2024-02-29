lista = [float(x) for x in input("Digite uma lista de números (Separe por espaços): ").split()]
numero_referencia = float(input("Digite um número de referência: "))
indice = next((i for i, numero in enumerate(lista) if numero > numero_referencia), None)
if indice is not None:
    print(f"O primeiro elemento maior que o numero {numero_referencia} esta na posição {indice}")
else:
    print(f"Não há elementos na lista maiores que o numero {numero_referencia}")
