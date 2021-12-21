from classes import Pessoa, Cliente, Aluno

"""
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
"""

pessoa = Pessoa("João", 18)
aluno = Aluno("Maria", 24)
cliente = Cliente("Antonio", 72)

pessoa.falar()
aluno.estudar()
cliente.comprar()

print()
print("#" * 50)
print()
