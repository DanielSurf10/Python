class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__

    def falar(self):
        print(f"{self.nomeClasse} está falando...")

    def __del__(self):
        print(f"{self.nomeClasse} FOI destruído")


class Cliente(Pessoa):
    def comprar(self):
        print(f"{self.nomeClasse} está comprando...")

    def __del__(self):
        print(f"{self.nomeClasse} FOI destruído")


class Aluno(Pessoa):
    def estudar(self):
        print(f"{self.nomeClasse} está estudando...")

    def __del__(self):
        print(f"{self.nomeClasse} FOI destruído")
