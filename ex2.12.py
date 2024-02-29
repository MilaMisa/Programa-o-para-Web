idade = int(input("Digite a idade da pessoa:"))
nacionalidade = input("Digite a nacionalidade da pessoa: ")

if idade >= 18 and (nacionalidade == 'brasil' or 'Brasil'): 
    print("Você pode votar!")
else:
    print("Você não pode votar!")
    