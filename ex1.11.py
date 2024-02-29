num1= int(input("Digite o primeiro numero (a): "))
num2= int(input("Digite o segundo numero (b): "))
num3= int(input("Digite o terceiro numero (c): "))

delta= (num2 ** 2)- 4 * num1 * num3
x1 = (-num2 + delta ** (1/2)) / (2 * num1)
x2 = (-num2 - delta ** (1/2)) / (2 * num1)
print("x1: {}, x2: {}".format(x1, x2))