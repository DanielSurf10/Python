# lista, str, tupla -> iterável

texto = "Bom dia"
iteravel = iter(texto)

# for letra in texto:
#     print(letra)

print(next(iteravel))
print(next(iteravel))
print(next(iteravel))

print("No for")

for valor in iteravel:
    print(valor)
