import math

PI = math.pi


def dobra(lista):
    return [x * 2 for x in lista]


def multiplca(lista):
    r = 1
    for i in lista:
        r *= i
    return r


# Se quiser apenas testar o módulo
# Execultando ele, ao invés de importar
if __name__ == "__main__":
    lista = range(1, 6)
    print(dobra(lista))
    print(multiplca(lista))
