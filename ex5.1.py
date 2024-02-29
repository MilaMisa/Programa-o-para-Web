import math
lista=list(range(21))


raiz=[math.sqrt(i) for i in lista if i % 2==0]


print(f"Raizes quadradas dos números pares de 0 a 20 : {raiz}")

