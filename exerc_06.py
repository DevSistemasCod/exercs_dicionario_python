def adicionar_contato(agenda):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone: ")
    email = input("Digite o email: ")
    # criação de um dicionário chamado de contato
    contato = {"Telefone": telefone, "Email": email}
    # o dicionário agenda possui nome como chave e contato como valor
    agenda[nome] = contato
    print(f"Contato {nome} adicionado com sucesso!")


def buscar_contato(agenda):
    nome = input("Digite o nome do contato a ser buscado: ")

    # se nome existe em agenda
    if nome in agenda:
        # atribui o conteúdo obtido para contato
        contato = agenda[nome]
        return contato
    else:
        return None


def remover_contato(agenda):
    nome = input("Digite o nome do contato a ser removido: ")

    if nome in agenda:
        del agenda[nome]
        print(f"Contato {nome} removido com sucesso!")
    else:
        print(f"Contato {nome} não encontrado.")


def menu():
    continuar = True
    agenda = {}
    
    while continuar:
        print("\nAgenda de Contatos")
        print("1. Adicionar Contato")
        print("2. Visualizar Contatos")
        print("3. Buscar Contato")
        print("4. Remover Contato")
        print("5. Sair")

        opcao = input("Escolha uma opção (1-5): ")

        if opcao == "1":
            adicionar_contato(agenda)
        elif opcao == "2":
            print("Agenda de Contatos: ",agenda)
        elif opcao == "3":
            resultado = buscar_contato(agenda)
            if resultado:
                print(resultado)
            else:
                print("Contato não encontrado.")
        elif opcao == "4":
            remover_contato(agenda)
        elif opcao == "5":
            print("Saindo do programa. Até mais!")
            continuar = False

        else:
            print("Opção inválida. Tente novamente.")


def main():
    menu()

if __name__ == "__main__":
    main()
