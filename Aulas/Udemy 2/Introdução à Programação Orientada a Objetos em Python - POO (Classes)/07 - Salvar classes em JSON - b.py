import json

CAMINHO = "Python/Aulas/Udemy 2/Introdução à Programação Orientada a Objetos em Python - POO (Classes)/"


class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


with open(CAMINHO + "classe.json", "r") as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)
