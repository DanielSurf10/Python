# Escopo da classe e de métodos da classe

class Animal:
    # nome = 'Leão'                     # Escopo da classe

    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'              # Escopo do método
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comando {alimento}'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


leao = Animal(nome='Leão')
print(leao.nome)
print(leao.executar('maçã'))
