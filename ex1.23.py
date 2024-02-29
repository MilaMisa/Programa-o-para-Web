distancia = float(input("Digite a distância percorrida: "))
tempo = int(input("Digite o tempo gasto: "))
aceleracao = float(input("Digite a aceleração: "))
velocidade_inicial = distancia/tempo - aceleracao * tempo / 2
velocidade_final = velocidade_inicial + aceleracao * tempo
print(f"A velocidade inicial é de {velocidade_inicial}m/s e a velocidade final é de {velocidade_final}")
