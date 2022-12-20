import json

CAMINHO = "Python/Aulas/Udemy 2/Introdução à Programação Orientada a Objetos em Python - POO (Classes)/"


class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)


def fazer_dump():
    with open(CAMINHO + "classe.json", "w") as arquivo:

        bd = [p1.__dict__, vars(p2), p3.__dict__]
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)


if __name__ == "__main__":              # O módulo for o main na execução:
    fazer_dump()
