from vendas import calc_preco
from vendas.formata.preco import real

preco = 49.90
preco_novo = calc_preco.aumento(preco, 15, True)
print(preco_novo)

preco_novo_desconto = calc_preco.desconto(preco, 15, True)
print(preco_novo_desconto)

print(real(50))
