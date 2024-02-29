familia = {}

for i in range(1, 6):
    nome = input(f'Digite o nome do {i}° membro da família: ')
    idade = int(input(f'Digite a idade do {i}° membro da família: '))
    cor_olhos = input(f'Digite a cor dos olhos do {i} membro da família: ')

    familia[f'membro{i}'] = {'nome': nome, 'idade': idade, 'cor_olhos': cor_olhos}

for membro, detalhes in familia.items():
    print(f'{membro}: {detalhes}')

