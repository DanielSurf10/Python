from itertools import zip_longest, count

indice = count()
cidades = ["São Paulo", 'Belo Horizonte', "Salvador", 'Bela Vista']
estados = ["Sp", "MG", "BA"]

cidades_estado_zip = list(zip(
    estados,
    cidades
))

print("Estados cidades zip:")
print(cidades_estado_zip)

cidades_estado_zip_longest = list(zip_longest(
    estados,
    cidades,
    fillvalue="Estado"
))

print("Estados cidades zip longest:")
print(cidades_estado_zip_longest)

cidades_estado_zip_count = list(zip(
    indice,
    estados,
    cidades
))

print("Cidade estados zip count")
print(cidades_estado_zip_count)

print("For cidade estados zip count")
for cont, estado, cidade in cidades_estado_zip_count:
    print(cont, estado, cidade)
