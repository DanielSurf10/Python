from itertools import permutations

def valido(tupla, lado, quantidade):
    contar_caixa = 1
    contador = 1

    if lado == "R":
        maior = tupla[-1]
        while (contador < 4):
            if maior < tupla[contador * -1]:
                contar_caixa += 1
                maior = tupla[contador * - 1]
            contador += 1
    else:
        maior = tupla[0]
        while (contador < 4):
            if maior < tupla[contador]:
                contar_caixa += 1
                maior = tupla[contador]
            contador += 1
    
    return contar_caixa == quantidade

def sequencial_linha(lista, pos):
    for i in range(tamanho):
        lista[i] = i + 1

def sequencial_coluna(lista, pos):
    for i in range(tamanho):
        lista[pos][i] = i + 1

P1 = permutations([1, 2, 3, 4], 4)
lista_perm = list(P1)

args = "4 3 2 1 1 2 2 2 4 3 2 1 1 2 2 2".split(' ')
args = [int(i) for i in args]
col_up = args[0:3]
col_down = args[4:7]
row_left = args[8:11]
row_right = args[12:15]

tamanho = 4

tabela = [0 for _ in range(tamanho * tamanho)]

# for item, count in zip(args, range(len(args))):
#     if item == 4:
#         if count >= 8:                                          # se for pra por numa linha
#             sequencial_linha(tabela, count)
#         if count < 8:                                           # se for pra por numa coluna
#             # sequencial_coluna(tabela, int(count / tamanho))
#             pass
    
        
# for i in tabela:
#     print(i)


L1 = list()
L2 = list()
L3 = list()
L4 = list()

print("L1")
for i in lista_perm:
    if valido(i, "L", 4):
        L1.append(i)
        print(i)

print("\nL2")
for i in lista_perm:
    if valido(i, "L", 3) and i[0] == 2:
        L2.append(i)
        print(i)

print("\nL3")
for i in lista_perm:
    if valido(i, "L", 2) and i[0] == 3:
        L3.append(i)
        print(i)

print("\nL4")
for i in lista_perm:
    if valido(i, "L", 1) and i[0] == 4 and i[3] == 3:
        L4.append(i)
        print(i)

R1 = list()
R2 = list()
R3 = list()
R4 = list()

print("\nR1")
for i in lista_perm:
    if valido(i, "R", 1):
        # i = tuple(reversed(i))
        R1.append(i)
        print(i)

print("\nR2")
for i in lista_perm:
    if valido(i, "R", 2) and i[0] == 2:
        # i = tuple(reversed(i))
        R2.append(i)
        print(i)

print("\nR3")
for i in lista_perm:
    if valido(i, "R", 2) and i[0] == 3:
        # i = tuple(reversed(i))
        R3.append(i)
        print(i)

print("\nR4")
for i in lista_perm:
    if valido(i, "R", 1) and i[0] == 4 and i[3] == 3:
        # i = tuple(reversed(i))
        R4.append(i)
        print(i)

print("\n\nIntersecção:")

Linha1 = list(set(L1).intersection(set(R1)))
Linha2 = list(set(L2).intersection(set(R2)))
Linha3 = list(set(L3).intersection(set(R3)))
Linha4 = list(set(L4).intersection(set(R4)))

print(Linha1)
print(Linha2)
print(Linha3)
print(Linha4)
