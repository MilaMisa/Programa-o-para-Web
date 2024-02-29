temperatura = float(input("Digite a temperatura:"))

if temperatura > 37:
    print("Temperatura acima do normal!")
elif temperatura < 36:
    print("Temperatura abaixo do normal!")
else:
    print("A temperatura está dentro da faixa normal (36°C a 37°C).")