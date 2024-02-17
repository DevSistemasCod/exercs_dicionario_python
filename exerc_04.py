def obter_lista_alunos():
    nomes_alunos = []
    continuar = True
    novo_cadastro = None

    while continuar:
        nome = input("Adicione um nome: ")
        nomes_alunos.append(nome)
        print("Cadastrar novo nome(s/n): ")
        novo_cadastro = input()
        if(novo_cadastro == "n"):
            continuar = False

    return nomes_alunos

def obter_lista_notas(nomes_alunos):
    notas_alunos = []
    continuar = True
    for aluno in nomes_alunos:
        # Solicitar ao usuário que insira a nota para cada aluno
        while continuar:
            nota = float(input(f"Digite a nota para {aluno}: "))
            if ((nota > 0) and (nota <= 10)):
                notas_alunos.append((aluno, nota))
                break
            else:
                print("Por favor, insira uma nota válida entre 0 e 10.")

    return notas_alunos


def ordenar_dicionario_por_nomes(dicionario):
    # utilizamos o método sorted() para efetutar a ordenação
    dicionario_ordenado = sorted(dicionario.items())
    return dicionario_ordenado
    

def main():
    alunos = obter_lista_alunos()
    notas = obter_lista_notas(alunos)

    # converte a lista de tuplas Nome Aluno, Nota Aluno
    # em um dicionário 
    dicionario_notas = dict(notas)
    dicionario_ordenado = ordenar_dicionario_por_nomes(dicionario_notas)
    print("Dicionário de Alunos e Notas:",dicionario_ordenado)

if __name__ == "__main__":
    main()
