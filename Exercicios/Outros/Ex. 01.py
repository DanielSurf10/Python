"""
1. Crie uma classe que modele uma pessoa
    (a) Atributos: nome, idade e endereço
    (b) Métodos: mostrar endereço e alterar endereço
"""


class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostrar_endereco(self):
        return self.endereco


