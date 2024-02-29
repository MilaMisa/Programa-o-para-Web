frase= input("Digite a frase: ")
substrings = [frase[i:i+6] for i in range(0, len(frase), 6)]
for substring in substrings:
    print(substring)
