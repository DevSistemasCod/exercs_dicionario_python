def adicionar_item(pessoas):
    nome = input("Informe o nome: ")
    idade = input("Informe a idade: ")
    # neste caso a chave será o nome e o valor a idade
    pessoas[nome] = idade
    print("Adicionado com sucesso !")


def remover_item_por_nome(pessoas):
    nome = input("Informe o nome que deseja remover: ")
    # criação de lista auxiliar
    # para evittar o erro de remoção de um item
    # do dicionário em tempo de execução
    chaves = list(pessoas.keys())
    item_encontrado = False

    # a iteração acontece sobre chaves em tempo de execução 
    # e não sobre o dicionário 
    for chave in chaves:
        # adicionamos o lower() para favorecer a validação 
        # o uso do lower() acontece apenas durante a claúsula if 
        if nome.lower() in chave.lower():
            del pessoas[chave]
            print(f"{nome} removido com sucesso!")
            item_encontrado = True
            break
    
    if item_encontrado == False:
        print(f"{nome} não encontrado")

# o método popitem() é capaz de remover o item adicionado
def remover_ultimo_item_adicionado(pessoas):
        chave, valor = pessoas.popitem()
        print(f"chave removida {chave} e valor removido {valor}")


def menu():
    pessoas = {}
    continuar = True

    while continuar:
        print("\n Cadastro de Pessoas")
        print("1 - Adicionar um novo item ")
        print("2 - Remover item por nome: ")
        print("3 - Remover último item adicionado ")
        print("4 - Exibir conteúdo do dicionário ")
        print("5 - Sair ")

        opcao = input("Informe a opção desejada (1-5): ")

        if opcao == "1":
            adicionar_item(pessoas)
        elif opcao == "2":
            remover_item_por_nome(pessoas)
        elif opcao == "3":
            remover_ultimo_item_adicionado(pessoas)
        elif opcao == "4":
            print("Dicionário de pessoas: ",pessoas)
        elif opcao == "5":
            continuar = False
            print(" Saindo...")
        else:
            print("Opção Inválida")    


def main():
    menu()


if __name__ == "__main__":
    main()