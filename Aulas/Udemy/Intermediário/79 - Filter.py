from dados import pessoas, produtos, lista

# filter
# Retorna uma lista apenas com os valores que atendem a condição da função dada como parâmetro

# Apenas os pares da lista
pares = filter(lambda x: x % 2 == 0, lista)
print(list(pares))

# Apenas valores que estão dentro de uma lista
lista_valores = [1, 1, 2, 3, 5, 8]
valores = filter(lambda x: x in lista_valores, lista)
print(list(valores))

# Com list comprehension
# Pares
pares = [i for i in lista if i % 2 == 0]
print(pares)

# Apenas valores que estão dentro de uma lista
valores = [i for i in lista if i in lista_valores]
print(valores)
