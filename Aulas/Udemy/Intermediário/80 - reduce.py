from dados import pessoas, produtos, lista
from functools import reduce

# Reduce

# Soma os valores da lista
soma_lista = reduce(lambda ac, i: ac + i, lista, 0)
print(soma_lista)

# Soma os preços dos produtos maiores que 20
soma_preco = reduce(lambda ac, i: ac + (i['preco'] if i['preco'] > 20 else 0), produtos, 0)
print(soma_preco)
