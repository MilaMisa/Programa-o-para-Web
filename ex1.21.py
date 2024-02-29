from math import sqrt
primeiro_lado = int(input("Digite o primeiro lado do triângulo: "))
segundo_lado = int(input("Digite o segundo lado do triângulo: "))
hipotenusa = sqrt(primeiro_lado**2 + segundo_lado**2)
print(f"A hipotenusa é igual a {hipotenusa}")
