
texto = input("Digite algo: ").upper()

caracteres = []
for i in texto:
    if i not in caracteres:
        caracteres.append(i)
caracteres.sort()

print(f"|-----------------|")
print(f"| Nº | char | qtd |")
print(f"|----|------|-----|")
for letra, i in zip(caracteres, range(1, len(caracteres) + 1)):
    qtd_letra = texto.count(letra)
    print(f"| {'' if i > 9 else 0}{i} |  {letra}   | {'' if qtd_letra > 9 else 0}{qtd_letra}  |")
print(f"|-----------------|")
