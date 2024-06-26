import os
from models.produto import Produto
from repo.produto import ProdutoRepo
from models.cliente import Cliente
from repo.cliente import ClienteRepo

ProdutoRepo.criar_tabela()

def obter_opcao() -> int:
    opcao = int(input("Opção Desejada: "))
    return opcao

def limpar_tela():
    os.system("cls") # tem que importar 'os'

def aguardar_enter():
    print("---------------------")
    print("Pressione ENTER para prosseguir...")
    input()

def inserir_produto():
    print("Inserção de Produto")
    print("-------------------")
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    descricao = input("Descrição: ")
    produto = Produto(None, nome, preco, descricao)
    #produto =Produto(nome=nome, preco=preco, descricao=descricao)
    ProdutoRepo.inserir(produto)

def listar_produtos():
    print("Listagem de Produtos")
    print("--------------------")
    produtos = ProdutoRepo.obter_todos()
    print(f"ID|Nome")
    for p in produtos:
        print(f"{p.id:02d}|{p.nome}")

def alterar_produto():
    print("Alterar Produto")
    print("---------------")
    id = int(input("Id do Produto: "))
    produto = ProdutoRepo.obter_um(id)
    novo_nome = input(f"Nome ({produto.nome}): ")
    novo_preco = float(input(f"Preço ({produto.preco:.2f}): "))
    nova_descricao = input(f"Descrição ({produto.descricao}): ")
    produto_alterado = Produto(id, novo_nome, novo_preco, nova_descricao)
    ProdutoRepo.alterar(produto_alterado)

def excluir_produto():
    print("Excluir Produto")
    print("---------------")
    id = int(input("Id do Produto: "))
    produto = ProdutoRepo.obter_um(id)
    resposta = input(f"Deseja realmente excluir o produto '{produto.nome}'? (S/N): ")
    if resposta.upper() == "S":
        ProdutoRepo.excluir(id)

def detalhes_produto():
    print("Detalhes do Produto")
    print("-------------------")
    id = int(input("Id do Produto: "))
    produto = ProdutoRepo.obter_um(id)
    print(f"Nome: {produto.nome}")
    print(f"Preço: {produto.preco:.2f}")
    print(f"Descrição: {produto.descricao}")

def mostrar_menu_produto():
    print("Menu Produto")
    print("--------------")
    print("1. Inserir Produto")
    print("2. Listar Produtos")
    print("3. Alterar Produto")
    print("4. Excluir Produto")
    print("5. Detalhes do Produto")
    print("6. Sair")
    print("--------------")


def menu_produto():
    while True:
        limpar_tela()
        mostrar_menu_produto()
        opcao = obter_opcao()
        limpar_tela()
        match(opcao):
            case 1:
                inserir_produto()
            case 2:
                listar_produtos()
            case 3:
                alterar_produto()
            case 4:
                excluir_produto()
            case 5:
                detalhes_produto()
            case 6:
                break
            case _:
                print("Opção Inválida!")
        aguardar_enter()
    print("Menu Produto finalizado com sucesso.")


ClienteRepo.criar_tabela()

def inserir_cliente():
    print("Inserção de Cliente")
    print("-------------------")
    nome = input("Nome: ")
    email = input("E-mail: ")
    telefone = int(input("Telefone: "))
    endereco = input("Endereço: ")
    senha = input("Senha: ")
    cliente = Cliente(None, nome, email, telefone, endereco, senha)
    ClienteRepo.inserir(cliente)

def listar_clientes():
    print("Listagem de Clientes")
    print("--------------------")
    clientes = ClienteRepo.obter_todos()
    print(f"ID|Nome")
    for p in clientes:
        print(f"{p.id:02d}|{p.nome}")

def alterar_cliente():
    print("Alterar Cliente")
    print("---------------")
    id = int(input("Id do Cliente: "))
    cliente = ClienteRepo.obter_um(id)
    novo_nome = input(f"Nome ({cliente.nome}): ")
    novo_email = input(f"E-mail ({cliente.email}): ")
    novo_telefone = int(input(f"Telefone ({cliente.telefone}): "))
    novo_endereco = input(f"Endereço ({cliente.endereco}): ")
    nova_senha = input(f"Senha ({cliente.senha}): ")
    cliente_alterado = Cliente(id, novo_nome, novo_email, novo_telefone, novo_endereco, nova_senha)
    ClienteRepo.alterar(cliente_alterado)

def excluir_cliente():
    print("Excluir Cliente")
    print("---------------")
    id = int(input("Id do Cliente: "))
    cliente = ClienteRepo.obter_um(id)
    resposta = input(f"Deseja realmente excluir o cliente '{cliente.nome}'? (S/N): ")
    if resposta.upper() == "S":
        ClienteRepo.excluir(id)

def detalhes_cliente():
    print("Detalhes do Cliente")
    print("-------------------")
    id = int(input("Id do Cliente: "))
    cliente = ClienteRepo.obter_um(id)
    print(f"Nome: {cliente.nome}")
    print(f"E-mail: {cliente.email}")
    print(f"telefone: {cliente.telefone}")
    print(f"Endereço: {cliente.endereco}")
    print(f"Senha: {cliente.senha}")

def mostrar_menu_cliente():
    print("Menu Cliente")
    print("--------------")
    print("1. Inserir Cliente")
    print("2. Listar Clientes")
    print("3. Alterar Cliente")
    print("4. Excluir Cliente")
    print("5. Detalhes do Cliente")
    print("6. Sair")
    print("--------------")



def menu_cliente():
    while True:
        limpar_tela()
        mostrar_menu_cliente()
        opcao = obter_opcao()
        limpar_tela()
        match(opcao):
            case 1:
                inserir_cliente()
            case 2:
                listar_clientes()
            case 3:
                alterar_cliente()
            case 4:
                excluir_cliente()
            case 5:
                detalhes_cliente()
            case 6:
                break
            case _:
                print("Opção Inválida!")
        aguardar_enter()
    print("Menu Cliente finalizado com sucesso.")




while True:
    print("Escolha sua opção: ")
    print("1.Produto")
    print("2.Cliente")
    print("3.Sair")
    escolha = int(input("Opção desejada: "))

    match(escolha):
            case 1:
                menu_produto()
            case 2:
                menu_cliente()
            case 3:
                break
            case _:
                print("Opção Inválida!")
    aguardar_enter()
print("Programa finalizado com sucesso.")