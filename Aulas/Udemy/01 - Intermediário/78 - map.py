from dados import produtos, pessoas, lista

# Map usa uma função para cada elemento de uma lista
nova_lista = map(lambda i: i*2, lista)
print(next(nova_lista))

# Pode também fazer com list comprehension
nova_lista_c = [i * 2 for i in lista]
print(nova_lista_c)


# com dicionários
def novo_preco(produto):
    produto['preco'] = round(produto['preco'] * 1.05, 2)
    return produto


novos_produtos = map(novo_preco, produtos)
print(list(novos_produtos))
