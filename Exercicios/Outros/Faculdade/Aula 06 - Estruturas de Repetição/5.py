# 5- Temos um grupo de pessoas. Escreva um programa em Python que leia o sexo e a
# altura de cada pessoa, calcule e mostre a altura média das mulheres e dos homens
# separadamente. Utilize o comando de repetição que desejar.

# Cria uma lista para armazenar as alturas de homens e mulheres separadamente
alturas_homens = []
alturas_mulheres = []

# Loop para ler as informações de altura e sexo de cada pessoa
for i in range(5):
    altura = float(input(f"Informe a altura da {i+1}ª pessoa: "))
    sexo = input(f"Informe o sexo da {i+1}ª pessoa (M/F): ")
    
    # Adiciona a altura na lista correspondente ao sexo
    if sexo == "M":
        alturas_homens.append(altura)
    elif sexo == "F":
        alturas_mulheres.append(altura)

# Calcula a altura média dos homens
if len(alturas_homens) > 0:
    media_homens = sum(alturas_homens) / len(alturas_homens)
    print(f"A altura média dos homens é: {media_homens:.2f} metros")
else:
    print("Não há homens no grupo.")

# Calcula a altura média das mulheres
if len(alturas_mulheres) > 0:
    media_mulheres = sum(alturas_mulheres) / len(alturas_mulheres)
    print(f"A altura média das mulheres é: {media_mulheres:.2f} metros")
else:
    print("Não há mulheres no grupo.")
