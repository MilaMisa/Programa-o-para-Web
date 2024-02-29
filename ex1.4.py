peso = float(input("Digite o seu peso(Kg): "))
altura = float(input("Digite a sua altura(m): "))

imc = (peso) / (altura ** 2)

print(f"O seu IMC é: {imc:.2f}")