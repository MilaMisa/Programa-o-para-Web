frase = input("Digite uma frase: ")
palavras = frase.split()
contagem_palavras = {}
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1

for palavra, aparicao in contagem_palavras.items():
    print(f"A palavra '{palavra}' aparece {aparicao} vezes ")
