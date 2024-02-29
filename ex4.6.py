print("Digite o primeiro número complexo:")
real1 = float(input("Parte real: "))
imag1 = float(input("Parte imaginária: "))
num1 = complex(real1, imag1)

print("\nDigite o segundo número complexo:")
real2 = float(input("Parte real: "))
imag2 = float(input("Parte imaginária: "))
num2 = complex(real2, imag2)

soma = num1 + num2
produto = num1 * num2

print(f"\nA soma dos números complexos é: {soma}")
print(f"O produto dos números complexos é: {produto}")
