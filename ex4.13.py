frase= input("Digite uma frase: ")
palavras = frase.split()
nova_frase = ' '.join(palavra.strip() for palavra in palavras)
print("Frase sem espaço:", nova_frase)
