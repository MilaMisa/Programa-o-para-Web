frase = input("Digite uma frase: ")
palavras = frase.split()
for i, palavra in enumerate(palavras, 1):
    print(f"A palavra '{palavra}' começa na posição: {i}")
