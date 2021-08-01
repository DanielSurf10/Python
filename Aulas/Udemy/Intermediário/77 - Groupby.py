from itertools import groupby, tee

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
    {'nome': 'José', 'nota': 'B'},
]

ordena = lambda i:i['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, key=ordena)

for agrupamento, agrupados in alunos_agrupados:
    agrupados1, agrupados2 = tee(agrupados)

    print(f"Agrupamento {agrupamento}")

    for aluno in agrupados1:
        print(f'\t{aluno["nome"]}')

    quantidade = len(list(agrupados2))
    print(f"{quantidade} alunos tiraram a nota {agrupamento}")

    print()
