lista_de_nomes = input("Digite uma lista de nomes (Separe por espaço) : ").split()
lista_de_notas = [float(x) for x in input("Digite uma lista de notas (Separe por espaço) : ").split()]
tuplas_decrescentes= sorted(zip(lista_de_nomes, lista_de_notas), key=lambda x: x[1], reverse=True)
print(f"Notas ordenadas: {tuplas_decrescentes}" )
