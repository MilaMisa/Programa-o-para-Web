valor_inicial = int(input("Digite o valor inicial do investimento: "))
taxa_juros = float(input("Digite a taxa de juros: "))
anos = int(input("Digite o número de anos: "))
montante = valor_inicial * (1 + taxa_juros)**anos
print(f"O valor final do investimento é de {montante}")
