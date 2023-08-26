numero_alunos = 5
media_notas = 6
cursos = ("ccp", "tabs")

nomes = []
notas = []
curso = []

for i in range(numero_alunos):
    nomes.append(input(f"Digite o nome do {i + 1}º aluno: "))
    notas.append(int(input(f"Digite a nota do {i + 1}º aluno: ")))
    curso.append(input(f"Digite o curso do {i + 1}º aluno [ ccp / tabs ]: "))

tabs = curso.count("tabs")
media = sum(notas) / numero_alunos
acima_media = sum([1 for i in notas if i >= media_notas])

print(f"Quantidade tabs: {tabs}")
print(f"Média: {media}")
print(f"Quantidade acima da média: {acima_media}")
