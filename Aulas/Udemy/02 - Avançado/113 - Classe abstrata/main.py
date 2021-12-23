from classes.cp import ContaPoupanca
from classes.cc import ContaCorrente


# a = Conta(111, 222, 0)                    # Mesmo que o método foi implementado,
#                                           # o decorador abstractmethod forçou a herança.
#                                           # Mas, se herdado e colocar só um "pass", já funciona
cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(1)

print('##########################')
cc = ContaCorrente(agencia=1111, conta=3333, saldo=0, limite=500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)
