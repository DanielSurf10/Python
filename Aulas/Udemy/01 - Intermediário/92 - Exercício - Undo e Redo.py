'''
Faça uma lista de tarefas com as seguintes apçães:
    [ 1 ] - adicionar tarefa
    [ 2 ] - remover tarefa
    [ 3 ] - listar tarefas
    [ 4 ] - opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    [ 5 ] - opção de refazer (a cada vez que chamarmos, refaz a última ação)
    [ 6 ] - sair

    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1']                <- Desfazer
    ['Tarefa 1', 'Tarefa 2']    <- Refazer
'''


def linha():
    print('-' * 50)


def cabecalho():
    linha()
    print("Programa".center(20, '-'))
    print("de".center(20, '='))
    print("Tarefas".center(20, '-'))
    linha()

    print("Escolha uma opção:")
    print("\t|-> [ 1 ] - Adicionar tarefa")
    print("\t|-> [ 2 ] - Remover tarefa")
    print("\t|-> [ 3 ] - Listar tarefas")
    print("\t|-> [ 4 ] - Desfazer última ação")
    print("\t|-> [ 5 ] - Refazer última ação")
    print("\t|-> [ 6 ] - Sair")
    return pegar_valor()


def pegar_valor(offset=6):
    while True:
        valor = input("Sua opção -> ")

        try:
            valor = int(valor)
            if 0 < valor < offset + 1:
                break
            else:
                print("Valor fora do intervalo. Tente novamente!")

        except ValueError:
            print("Valor inválido. Tente novamente!")

        print('-' * 35)

    return int(valor)


def adicionar(lista):
    linha()
    print("Adicionar tarefa:")

    nome = input("Infome o nome -> ")
    lista.append(nome)

    linha()
    print(f'Tarefa [ {nome} ] adicionada.')
    desfazer.append([nome, -1, 0])


def remover(lista):
    linha()
    print("Remover tarefa:", end='\n\n')
    listar(lista, "Qual deseja remover")

    opcao_remover = pegar_valor(len(lista))
    desfazer.append([lista[opcao_remover - 1], opcao_remover - 1, 1])

    del lista[opcao_remover - 1]


def listar(lista, texto=''):
    print(texto.center(27))
    print('-' * 27)
    print(f"| Nº |{'Nome'.center(20)}|")
    print('-' * 27)
    for num, valor in enumerate(lista):
        print(f"|{num + 1:^4}|{valor.center(20)}|")
    print('-' * 27)


def desfazer_acao(lista):
    global num_de_tarefa

    if desfazer[-1][2] == 0:    # Desfazer adicionar
        lista.pop()
        num_de_tarefa -= 1
        refazer.append(desfazer.pop())

    else:                       # Refazer adicionar
        lista.insert(desfazer[-1][1], desfazer[-1][0])
        num_de_tarefa += 1
        refazer.append(desfazer.pop())

    print("Desfeito!")


def refazer_acao(lista):
    global num_de_tarefa

    if refazer[-1][2] == 0:  # Refazer adicionar
        lista.append(refazer[-1][0])
        num_de_tarefa += 1
        desfazer.append(refazer.pop())

    else:
        del lista[refazer[-1][1]]
        num_de_tarefa -= 1
        desfazer.append(refazer.pop())

    print("Refeito!")


tarefas  = []
desfazer = []           # 0 - Adicionar
refazer  = []           # 1 - Remover

# Nome   Indice   Ação
# [Nome,   -1,     0]
# [Nome,   -1,     1]
# [Nome,    2,     1]

num_de_tarefa = 0

opcao = 0

while opcao != 6:
    opcao = cabecalho()

    # Adicionar tarefa
    if opcao == 1:
        adicionar(tarefas)
        num_de_tarefa += 1

    # Remover tarefa
    if opcao == 2:
        if num_de_tarefa < 1:
            print("Nenhuma tarefa para remover!")

        else:
            remover(tarefas)
            num_de_tarefa -= 1

    # listar tarefas
    if opcao == 3:
        print()
        listar(tarefas, "Lista de tarefas")

    # Desfazer
    if opcao == 4:
        if len(desfazer) < 1:
            print("Nada para desfazer!")

        else:
            desfazer_acao(tarefas)

    # Refazer
    if opcao == 5:
        if len(refazer) < 1:
            print("Nada para refazer!")

        else:
            refazer_acao(tarefas)

    # Limpar a tela
    print('\n' * 3)
