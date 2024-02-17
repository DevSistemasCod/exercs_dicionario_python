def criar_dicionario_palavras(lista_palavras):
    dicionario_comprimentos = {}
    for palavra in lista_palavras:
        #criamos o dicionário usando a palavra como chave
        # e o comprimento dela como valor
        dicionario_comprimentos[palavra] = len(palavra)

    return dicionario_comprimentos


def main():
    entrada_usuario = input("Digite uma lista de palavras separadas por espaço: ")
    lista_palavras = entrada_usuario.split()
    dicionario = criar_dicionario_palavras(lista_palavras)
    print("Dicionário de Palavras:",dicionario)

if __name__ == "__main__":
    main()
