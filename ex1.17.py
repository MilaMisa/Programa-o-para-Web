preco = int(input("Digite o preco da mercadoria: "))
desconto = float(input("Digite o desconto da mercadoria: "))
imposto = float(input("Digite o imposto sobre a mercadoria: "))
preco_final = preco * (1 +imposto/100) * (1-desconto/100)
print(f"O preço final da mercadoria é de {preco_final}")