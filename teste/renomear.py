import os
from random import randint

path = "Python/teste/renomear"
lista = os.listdir(path)
a = randint(0, 10)
lista2 = [a + i for i in range(len(lista))]

for i, j in zip(lista, lista2):
    antigo = f'{path}/{i}'
    novo = f'{path}/a{j}.txt'
    os.rename(antigo, novo)
