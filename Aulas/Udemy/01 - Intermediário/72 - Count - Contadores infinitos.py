from itertools import count

contador = count()

print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))

for valor in contador:
    print(valor)

    if valor >= 10:
        break

com_inicio = count(start=7)

print(next(com_inicio))
print(next(com_inicio))

com_step = count(start=10, step=5)

for valor in com_step:
    print(valor)

    if valor >= 30:
        break

step_com_float = count(step=1.5)

for valor in step_com_float:
    print(valor)

    if valor >= 5:
        break
