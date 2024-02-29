frase = input("Digite uma frase: ")
artigos = ['o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas']
palavras = frase.split()
nova_frase = ' '.join(palavra for palavra in palavras if palavra.lower() not in artigos)
print("Frase sem artigos:", nova_frase)
