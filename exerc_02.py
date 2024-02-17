
def adicionar(qtd_elementos):
    lista = []

    for i in range(qtd_elementos):
        num = int(input("Entre com um número: "))
        lista.append(num)
    
    return lista

def analisar_numeros(lista):
    # Verifica se a lista não está vazia
    if not lista:
        return None  # Retorna None se a lista estiver vazia
    
    # Calcula as informações
    media = sum(lista) / len(lista)
    maximo = max(lista)
    minimo = min(lista)
    quantidade = len(lista)
    
    # Cria o dicionário com as informações
    resultado = {
        'media': media,
        'maximo': maximo,
        'minimo': minimo,
        'quantidade': quantidade
    }
    
    return resultado

def main():
    qtd_elementos = int(input("Informe a quantidade de elementos da lista: "))
    numeros = adicionar(qtd_elementos)

    # Chama a função e exibe o resultado
    resultado = analisar_numeros(numeros)
    
    print("Dicionário: ",resultado)

if __name__ == "__main__":
    main()
