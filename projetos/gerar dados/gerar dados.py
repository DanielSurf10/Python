# coding=UTF-8

from random import randint

nomes     = []
pessoas   = []
regioes   = []


class Pessoa:
    def __init__(self):
        self.nome    = nomes[randint(0, 49)]
        self.idade   = randint(10, 70)
        self.tamanho = randint(130, 160) / 100 if self.idade < 15 else randint(150, 198) / 100
        regiao       = regioes[randint(0, 25)].split("-")
        self.regiao  = regiao[0]
        self.cidade  = regiao[1]


arq = open("projetos\\gerar dados\\nomes.txt", "r")
nomes = arq.read().split("\n")
arq.close()

arq = open("projetos\\gerar dados\\regioes.txt", "r")
regioes = arq.read().split("\n")
arq.close()

for i in range(200):
    pessoas.append(Pessoa())

arq = open("projetos\\gerar dados\\dados.csv", "w")
for i in pessoas:
    arq.write(f"{i.nome},{i.idade},{i.tamanho},{i.regiao},{i.cidade}\n")
arq.close()
