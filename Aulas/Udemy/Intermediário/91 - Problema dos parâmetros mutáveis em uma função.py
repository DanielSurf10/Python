# Com o problema
def juntar(num, lista=[]):
    lista.append(num)
    return lista


a = juntar(1)           # Vai juntar a lista que foi declada junto com a função com o 1
b = juntar(2)           # Vai juntar a lista que já tinha o valor 1, com o 2
c = juntar(3, [1, 2])   # Não deu problema, porque usou uma lista própria, e não a da função

print("Com problema")
print(a)
print(b)
print(c)
print("-" * 20, end="\n\n")


# Solução
def juntar_certo(num, lista=None):
    if lista is None:
        lista = []

    lista.append(num)
    return lista


a = juntar_certo(1)
b = juntar_certo(2)
c = juntar_certo(3, [1, 2])

print("Com problema")
print(a)
print(b)
print(c)
