def e_palindromo (palavra):	return palavra == palavra[::-1]palavra = input("Digite uma palavra: ") if e_palindromo(palavra):    print("Essa palavra é um palíndromo!")else:    print("Essa palavra não é um palíndromo!")