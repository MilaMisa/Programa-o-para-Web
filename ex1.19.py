velocidade_inicial = int(input("Digite a velocidade inicial: "))
velocidade_final = int(input("Digite a velocidade final: "))
tempo = float(input("Digite a variação de tempo: "))
aceleracao = (velocidade_final - velocidade_inicial)/tempo
print(f"A aceleração é de {aceleracao}")