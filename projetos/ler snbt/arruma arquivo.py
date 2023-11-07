with open('projetos/ler snbt/original/chapters/chapter_m4.snbt', 'r') as arquivo:
	snbt = arquivo.read()

a = snbt.split('\n')

for i in range(1, len(a) - 2):
	linha_atual = a[i].strip()
	linha_proxima = a[i + 1].strip()
	if linha_atual[-1] == '{' or linha_atual[-1] == '[':
		continue
	if (linha_proxima[-1] == '}' or linha_proxima[-1] == ']') and not linha_proxima[0].isalpha():
		continue
	a[i] = f'{a[i]},'

a = '\n'.join(a)

print(a)
