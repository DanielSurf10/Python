from eletronico import Eletronico
from log import LogMixin


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def ligar(self):
        if self._ligado:
            erro = f"{self._nome} já está ligado."
            print(erro)
            self.log_error(erro)
            return

        super().ligar()
        info = f"{self._nome} foi ligado."
        print(info)
        self.log_info(info)

    def desligar(self):
        if not self._ligado:
            erro = f"{self._nome} já está desligado."
            print(erro)
            self.log_error(erro)
            return

        if self._conectado:
            self.desconectar()

        super().desligar()
        info = f"{self._nome} foi desligado."
        print(info)
        self.log_info(info)

    def conetar(self):
        if not self._ligado:
            erro = f'{self._nome} não está ligado.'
            print(erro)
            self.log_error(erro)
            return

        if self._conectado:
            error = f'{self._nome} já está conectado.'
            print(error)
            self.log_error(error)
            return

        self._conectado = True
        info = f'{self._nome} foi conectado.'
        print(info)
        self.log_info(info)

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} já está desconectado.'
            print(error)
            self.log_error(error)
            return

        self._conectado = False
        info = f'{self._nome} foi desconectado.'
        print(info)
        self.log_info(info)
