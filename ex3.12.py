def e_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
    
soma = 0
for numero in range(1, 101):
    if e_primo(numero):
        soma += numero
print(f"A soma dos números primos de 1 a 100 é igual a {soma}")
