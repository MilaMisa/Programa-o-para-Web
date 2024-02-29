from math import sqrt
distancia = int(input("Digite a distancia: "))
velocidade_inicial = int(input("Digite a velocidade inicial: "))
tempo = sqrt(2*distancia/velocidade_inicial)
print(f"O tempo de queda livre para o objeto atingir o solo é de {tempo:.2} segundos")
