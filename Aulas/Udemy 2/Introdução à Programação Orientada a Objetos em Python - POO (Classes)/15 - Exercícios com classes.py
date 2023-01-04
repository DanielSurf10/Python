# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Motor:
    def __init__(self, nome):
        self.nome = nome


class Carro:
    def __init__(self, nome, fabricante, ano, motor):
        self.nome = nome
        self.fabricante = fabricante
        self.motor = motor
        self.ano = ano
    
    def QuemSouEu(self):
        print(f"{self.fabricante.nome} {self.nome} {self.motor.nome} {self.ano}")


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


fabricante = Fabricante("Faz Carro")
carro1 = Carro("Carro", fabricante, 2010, Motor("1.0"))
carro2 = Carro("Arroc", fabricante, 2015, Motor("2.0"))

carro1.QuemSouEu()
carro2.QuemSouEu()
