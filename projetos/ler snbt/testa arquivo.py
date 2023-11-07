file = "projetos/ler snbt/original/chapters/progression.snbt"

with open(file, 'r') as arq:
	a = arq.read()

numero = 8225

print(a[numero - 100:numero + 100])
