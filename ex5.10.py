lista = input("Digite uma lista de palavras (Separe por espaço): ").split()
comprimento = list(map(len, lista))
print(f"Comprimento das palavras:  {comprimento}")
