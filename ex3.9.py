print("Numeros divisíveis por 3 ou 5 entre 1 e 100: ")
for i in range(1,101):
    if i % 3 == 0 or i % 5 == 0:
        print(i)