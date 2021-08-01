from pessoas import Pessoa

p1 = Pessoa('João', 20)
p2 = Pessoa('Paula', 32)

p1.comer('maçã')
p1.falar('abobora')
p1.parar_falar()
p1.parar_comer()
p1.parar_comer()

p2.falar('coisas')
p2.comer("algo")
p2.parar_comer()
p2.parar_falar()
p2.parar_falar()

print(f'{p1.nome} nasceu em {p1.ano_nacimento()}.')
print(f'{p2.nome} nasceu em {p2.ano_nacimento()}.')
