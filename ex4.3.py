import math

angulo= int(input("Digite um ângulo (em graus): "))

seno=math.sin(math.radians(angulo))
cosseno=math.cos(math.radians(angulo))
tangente=math.tan(math.radians(angulo))

print(f"O seno de {angulo} graus é: {seno}, o cosseno de {angulo} graus é: {cosseno} e a tangente de {angulo} graus é: {tangente}")