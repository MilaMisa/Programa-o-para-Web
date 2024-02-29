import nltk
def pedir_frase():
    while True:
        frase = input("Digite uma frase com 5 palavras: ")
        palavras = nltk.word_tokenize(frase)
        if len(palavras) == 5:
            return palavras
        else:
            print("A frase não tem 5 palavras. Tente novamente.")
frase = pedir_frase()
for palavra in frase:
    print(palavra)

#Não consegui testar pois não consegui acessar a biblioteca!