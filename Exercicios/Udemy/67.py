carrinho = list()

carrinho.append(("Produto 1", 20))
carrinho.append(("Produto 2", "30"))
carrinho.append(("Produto 3", 50))

total = sum([float(x[1]) for x in carrinho])

print(total)
