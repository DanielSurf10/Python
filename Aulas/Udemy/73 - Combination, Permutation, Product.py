from itertools import combinations, permutations, product

pessoas = ["Luiz", "Letícia", "Amanda", "André", "Júlia"]

# Sem repetição, ordem não importa
# combinations(lista, quantidade_de_individuos)
for grupos in combinations(pessoas, 2):
    print(grupos)

print()

# Com repetição, ordem importa
# permutations(lista, quantidade_de_individuos)
for grupos in permutations(pessoas, 2):
    print(grupos)

print()

# Com repetição, repete o mesmo
# product(lista, repeat=quantidade_de_individuos)
for grupos in product(pessoas, repeat=2):
    print(grupos)

print()

# Combinations com mais indivíduos
for grupos in combinations(pessoas, 3):
    print(grupos)
