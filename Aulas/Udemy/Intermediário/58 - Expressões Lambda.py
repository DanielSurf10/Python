# lista
lista = [
    ["P1", 12],
    ["P2", 50],
    ["P3", 24],
    ["P4", 33],
    ["P5", 74]
]


# Ordenamento
# Função normal
def f(i):
    return i[1]


# Função anônima
fa = lambda i: i[1]

# Executando - sorted
print("Função normal")
print(sorted(lista, key=f))

print()

print('Função Anônima')
print(sorted(lista, key=fa))

print()

# Executando - sort
print("Expressão lambda")
lista.sort(key=lambda i: i[1])
print(lista)
