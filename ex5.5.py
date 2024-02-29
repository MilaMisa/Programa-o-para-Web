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


alunos_aprovados = {chave: valor for chave, valor in dicionario.items() if valor>=7}
print(alunos_aprovados)














  