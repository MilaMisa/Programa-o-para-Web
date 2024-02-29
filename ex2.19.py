numero1 = int(input("Digite o primeiro número inteiro:"))
numero2 = int(input("Digite o segundo número inteiro:"))
numero3 = int(input("Digite o terceiro número inteiro:"))
numero4 = int(input("Digite o quarto número inteiro:"))
numero5 = int(input("Digite o quinto número inteiro:"))

if numero1 % 2 == 0 and numero2 % 2 == 0 and numero3 % 2 == 0 and numero4 % 2 == 0 and numero5 % 2 == 0:
    print("Todos os números digitados são pares!")
else:
    print("Há pelo menos um número ímpar!")
    