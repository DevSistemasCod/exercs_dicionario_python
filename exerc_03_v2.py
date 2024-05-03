
def cria_lista(tamanho):
    lista_palavras = []

    for i in range(tamanho):
        palavra = input("Entre com a palavra: ")
        lista_palavras.append(palavra)
    
    return lista_palavras


def criar_dicionario(lista_palavras):
    dicionario = {}
    for palavra in lista_palavras:
        dicionario[palavra] = len(palavra)
    
    return dicionario

def main():
    tamanho = int(input("Entre com o tamanho da lista: "))
    lista_palavras = cria_lista(tamanho)
    dicionario_novo = criar_dicionario(lista_palavras)
    print(dicionario_novo)


if __name__ == "__main__":
    main()