from classes import CarrinhoDeCompras, Produto

# Agregação é um tipo de associação
# Mas assim como um carro não funciona sem as rodas
# A classe não vai funcionar sem a outra, mesmmo os dois existindo independentemente um do outro

carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)
p2 = Produto('iPhone', 10000)
p3 = Produto('Caneca', 15)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
# carrinho.inserir_produto(p1)
# carrinho.inserir_produto(p1)
# carrinho.inserir_produto(p2)
# carrinho.inserir_produto(p3)

carrinho.lista_produto()
print(carrinho.soma_total())

del carrinho

print()
