import json

with open("projetos/gerar json norminette/pegar.json", 'r') as arq:
	novo = json.load(arq)

with open("projetos/gerar json norminette/gerado.json", 'r') as arq:
	juntar = json.load(arq)


# for keys in novo.keys():
# 	juntar[keys] = []

for keys in novo.keys():
	juntar[keys].append(novo[keys])

# print(juntar)

with open("projetos/gerar json norminette/gerado.json", 'w', encoding='utf8') as arq:
	json.dump(juntar, arq, indent='\t', ensure_ascii=False)
