nome_produto = input("Digite o nome do produto: ")
preco_custo = float(input("Digite o preço de custo do produto: "))
preco_venda = float(input("Digite o preço de venda do produto: "))
qtde_estoque = int(input("Digite a quantidade em estoque do produto: "))
lucro_unitario = preco_venda - preco_custo
lucro_total = lucro_unitario * qtde_estoque
print(f"O lucro que esse estoque de {nome_produto} pode gerar é de R${lucro_total:.2f}")