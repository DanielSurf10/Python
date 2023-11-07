from nbtlib import parse_nbt, serialize_tag
from nbtlib.tag import String
import json


def arruma_snbt(snbt):
	a = snbt.split('\n')

	if (a[1][-1] == ','):
		return snbt
	for i in range(1, len(a) - 2):
		linha_atual = a[i].strip()
		linha_proxima = a[i + 1].strip()
		if linha_atual[-1] == '{' or linha_atual[-1] == '[':
			continue
		if (linha_proxima[-1] == '}' or linha_proxima[-1] == ']') and not linha_proxima[0].isalpha():
			continue
		a[i] = f'{a[i]},'
	return '\n'.join(a)


linhas = {}
dict_quests = {'progression':		'progression.snbt',
			   'tips':				'tips.snbt',
			   'market':			'quests.snbt',
			   'chapter.0':			'chapter_0_beginnings.snbt',
			   'chapter.1':			'chapter_1_the_andesite_age.snbt',
			   'chapter.2':			'sad.snbt',
			   'chapter.3':			'chapter_3.snbt',
			   'chapter.4':			'chapter_4.snbt',
			   'chapter.5':			'chapter_5.snbt',
			   'chapter.6_finale':	'chapter_6_finale.snbt',
			   'chapter.m1':		'chapter_m1.snbt',
			   'chapter.m2':		'chapter_m2.snbt',
			   'chapter.m3':		'chapter_m3.snbt',
			   'chapter.m4':		'chapter_m4.snbt'
			   }

for chapter_name, file_name in dict_quests.items():

	print(chapter_name)

	with open(f'original/chapters/{file_name}', 'r') as arquivo:
		snbt_string = arquivo.read()

	snbt_string = arruma_snbt(snbt_string)

	capitulo = parse_nbt(snbt_string)
	texto_capitulo = f"{chapter_name}.quest"

	# get title do capítulo
	# linhas[f"{texto_capitulo}.id"] = capitulo['id']
	try:
		linhas[f"{texto_capitulo}.title"] = capitulo['title']
		capitulo['title'] = String(f"{'{'}{texto_capitulo}.title{'}'}")
	except KeyError:
		# linhas[f"{texto_capitulo}.title"] = ""
		pass

	# Para cada quest faça
	for i in range(len(capitulo['quests'])):

		# get id
		# linhas[f"{texto_capitulo}.{i + 1}.id"] = capitulo['quests'][i]['id']

		# get title
		try:
			linhas[f"{texto_capitulo}.{i + 1}.title"] = capitulo['quests'][i]['title']
			capitulo['quests'][i]['title'] = String(f"{'{'}{texto_capitulo}.{i + 1}.title{'}'}")
		except KeyError:
			# linhas[f"{texto_capitulo}.{i + 1}.title"] = ""
			pass

		# get subtitle
		try:
			linhas[f"{texto_capitulo}.{i + 1}.subtitle"] = capitulo['quests'][i]['subtitle']
			capitulo['quests'][i]['subtitle'] = String(f"{'{'}{texto_capitulo}.{i + 1}.subtitle{'}'}")
		except KeyError:
			# linhas[f"{texto_capitulo}.{i + 1}.subtitle"] = ""
			pass

		# get description
		try:
			descriptions_all = list(capitulo['quests'][i]['description'])
			descriptions = descriptions_all.copy()

			# Tira as descrições que são strings vazias
			if ('' in descriptions):
				descriptions = [x for x in descriptions if x != '']

			tamanho_description = len(descriptions)

			# Para cada descrição faça
			for description_item in range(tamanho_description):
				linhas[f"{texto_capitulo}.{i + 1}.description.{description_item + 1}"] = descriptions[description_item]
				index_description = descriptions_all.index(descriptions[description_item])
				capitulo['quests'][i]['description'][index_description] = String(f"{'{'}{texto_capitulo}.{i + 1}.description.{description_item + 1}{'}'}")
		except KeyError:
			# linhas[f"{texto_capitulo}.{i + 1}.description.1"] = ""
			pass


		# get tasks
		try:
			tasks = list(capitulo['quests'][i]['tasks'])
			title_task = tasks[0]['title']
			linhas[f"{texto_capitulo}.{i + 1}.task.1.title"] = title_task
			capitulo['quests'][i]['tasks'][0]['title'] = String(f"{'{'}{texto_capitulo}.{i + 1}.task.1.title{'}'}")
		except KeyError:
			pass



	snbt_string = serialize_tag(capitulo, indent='\t')

	with open(f'novo/{file_name}', 'w') as arquivo:
		arquivo.write(snbt_string)

with open('novo/en_us.json', 'w') as arquivo:
	json.dump(linhas, arquivo, indent='\t')
