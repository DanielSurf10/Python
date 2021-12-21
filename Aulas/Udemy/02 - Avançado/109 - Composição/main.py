from classes import Cliente

# Composição é a relação de classes mais forte
# Nela todas as classes pertecem a principal
# Se a principal for deletada, todas são

cliente1 = Cliente("Jõao", 55)
cliente1.adicionar_endereco("Ali", "SP")
print(f"{cliente1.nome}")
cliente1.listar_enderecos()
del cliente1

print()
cliente2 = Cliente("Ana", 18)
cliente2.adicionar_endereco("Aqui", "BA")
cliente2.adicionar_endereco("Lá", "BH")
print(f"{cliente2.nome}")
cliente2.listar_enderecos()

print()
cliente3 = Cliente("Joana", 30)
cliente3.adicionar_endereco("Sei lá", "AM")
print(f"{cliente3.nome}")
cliente3.listar_enderecos()

print("#" * 50)
