import json

with open("projetos/gerar json norminette/pegar.json", 'r') as arq:
	novo = json.load(arq)

with open("projetos/gerar json norminette/gerado.json", 'r') as arq:
	gerado = json.load(arq)


for keys in novo.keys():
	try:
		if (novo[keys] not in gerado[keys]):
			if (isinstance(novo[keys], list)):
				gerado[keys].extend(novo[keys])
			else:
				gerado[keys].append(novo[keys])
	except KeyError:
		if (isinstance(novo[keys], list)):
			gerado[keys] = novo[keys].copy()
		else:
			gerado[keys] = [novo[keys]]

# print(gerado)

with open("projetos/gerar json norminette/gerado.json", 'w', encoding='utf8') as arq:
	json.dump(gerado, arq, indent='\t', ensure_ascii=False)
