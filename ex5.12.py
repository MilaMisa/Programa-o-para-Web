lista_chaves = input("Digite uma lista de chaves (Separe por espaço) : ").split()
lista_valores = input("Digite uma lista de valores (Separe por espaço) : ").split()
dicionario = dict(zip(lista_chaves, lista_valores))
print(dicionario)
