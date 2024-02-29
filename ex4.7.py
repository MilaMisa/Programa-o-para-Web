import re
nome = input("Digite um nome de usuário com apenas caracteres alfanuméricos: ")
senha = input("Digite uma senha com apenas caracteres alfanuméricos: ")

if nome.isalnum() == False:
    nome_sem_especiais = re.sub('[^A-Za-z0-9]+', '', nome)
    print(f"Nome alterado para: {nome_sem_especiais}")
if senha.isalnum() == False:
    senha_sem_especiais = re.sub('[^A-Za-z0-9]+', '', senha)
    print(f"Senha alterada para: {senha_sem_especiais}")
else: print("Nenhum valor modificado")

