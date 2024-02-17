
def adicionar_produto(inventario):
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade em estoque: "))

    # criamos um dicionário com código como sendo a chave
    # o valor é um dicionário com as informações nome, preço e quantidade
    inventario[codigo] = {'nome': nome, 'preco': preco, 'quantidade': quantidade}
    print("\nProduto adicionado com sucesso!")

# No método abaixo cada item pode ser atualizado separadamente
def atualizar_produto(inventario):
    codigo = input("Digite o código do produto que deseja atualizar: ")
    
    if codigo in inventario:
        print("Produto encontrado. Atualize as informações (pressione Enter para manter as informações existentes):")
        
        novo_nome = input(f"Novo nome ({inventario[codigo]['nome']}): ")
        if novo_nome != "":
            inventario[codigo]['nome'] = novo_nome

        novo_preco = input(f"Novo preço ({inventario[codigo]['preco']}): ")
        if novo_preco != "":
            inventario[codigo]['preco'] = float(novo_preco)

        nova_quantidade = input(f"Nova quantidade em estoque ({inventario[codigo]['quantidade']}): ")
        if nova_quantidade != "":
            inventario[codigo]['quantidade'] = int(nova_quantidade)

        print("Informações do produto atualizadas com sucesso.")
    else:
        print("Produto não encontrado no inventário.")


def remover_produto(inventario):
    codigo = input("Digite o código do produto que deseja remover: ")

    # se código informado pelo usuário existe no dicionádio chamado inventario
    if codigo in inventario:
        # a exclusão é feita com base na chave
        del inventario[codigo]
        print(f"\nProduto removido com sucesso!\n")
    else:
        print(f"\nProduto com código {codigo} não encontrado.\n")

def main():
    contunuar = True
    inventario = {}

    while contunuar:
        print("\nMenu:")
        print("1. Adicionar produto")
        print("2. Exibir inventário")
        print("3. Atualizar produto")
        print("4. Remover produto")
        print("5. Sair")

        escolha = input("\nEscolha uma opção: ")

        if escolha == '1':
            adicionar_produto(inventario)
        elif escolha == '2':
            print("Exibir Conteúdo: ", inventario)
        elif escolha == '3':
            atualizar_produto(inventario)
        elif escolha == '4':
            remover_produto(inventario)
        elif escolha == '5':
            print("Saindo...")
            contunuar = False
        else:
            print("Opção inválida!!!")

if __name__ == "__main__":
    main()
