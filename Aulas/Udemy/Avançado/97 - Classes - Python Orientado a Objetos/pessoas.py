from datetime import datetime


class Pessoa:
    ano_atual = datetime.now().year

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, comida):
        if self.comendo:
            print(f'{self.nome} já está comendo {comida}.')
            return

        if self.falando:
            print(f"{self.nome} não pode comer falando.")
            return

        print(f'{self.nome} está comendo {comida}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def falar(self, assunto):
        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def ano_nacimento(self):
        return self.ano_atual - self.idade

    @classmethod
    def por_ano(cls, nome, ano):
        idade = cls.ano_atual - ano
        return cls(nome, idade)
