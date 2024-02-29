primeira_lista = [float(x) for x in input("Digite a primeira lista de números (Separe por espaço): ").split()]
segunda_lista = [float(x) for x in input("Digite a segunda lista de números (Separe por espaço): ").split()]
media = list(map(lambda x, y: (x + y) / 2, primeira_lista, segunda_lista))
print("Médias dos elementos :", media)
