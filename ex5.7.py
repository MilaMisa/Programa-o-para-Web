dicionario = {}
chave = ""
valor = ""

while True:
    chave = (input("Digite o nome do aluno (x para parar): "))
    if chave != "x":
        valor =float(input("Digite a nota do aluno: "))
        dicionario[chave] = valor 
    else:
        break

notas_arredondadas = {chave: round(valor) for chave, valor in dicionario.items()}

print("Dicionário de Alunos e Notas:")
print(dicionario)

print("Dicionário de Alunos e Notas Arredondadas:")
print(notas_arredondadas)





