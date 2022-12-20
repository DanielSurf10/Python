# Introdução ao método __init__ (inicializador de atributos)
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
#
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:                                       # Criação da classe
    def __init__(self, nome, sobrenome):                # Metodo de inicialização do objeto - primeiro parâmetro é self
        self.nome = nome                                    # Atributos da classe
        self.sobrenome = sobrenome


p1 = Pessoa('Luiz', 'Otávio')                       # Instanciação do objeto p1 com atributos
# p1.nome = 'Luiz'
# p1.sobrenome = 'Otávio'

p2 = Pessoa('Maria', 'Joana')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)
