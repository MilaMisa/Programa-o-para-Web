CONSOANTES = "abcdfghjklmnpqrstvwxyz"
VOGAIS = "aeiou"
letra = input("Digite uma letra: ")
if len(letra) == 1:
    if letra in VOGAIS:
        print("Você digitou uma vogal.")
    elif letra in CONSOANTES:
        print("Você digitou uma consoante.")
    else: 
        print("Você não digitou uma letra.")
else:
    print("Você digitou mais de um caractere.")