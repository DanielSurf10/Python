class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__

    def falar(self):
        print(f"{self.nomeClasse} está falando...")


class Cliente(Pessoa):
    def comprar(self):
        print(f"{self.nomeClasse} está comprando...")

    def falar(self):
        print(f"{self.nome} - Estou em Cliente")


class ClienteVIP(Cliente):
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)                          # Quando referencia a classe pelo nome, precisa do self
        super().falar()                             # Quando referencia a classe pelo super(), não precisa do self
        print(f"{self.nome} {self.sobrenome}")
