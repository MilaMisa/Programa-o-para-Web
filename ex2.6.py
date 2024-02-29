palavra = input("Digite uma palavra:") #inverter a string inteira [::-1] 
palindromo = palavra[::-1]
if palavra == palindromo:
    print("Essa palavra é um palíndromo!")
else:
    print("Essa palavra não é um palíndromo!")