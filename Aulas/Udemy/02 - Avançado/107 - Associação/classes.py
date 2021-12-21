class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None        # Associa uma clase inteira dentro de outra classe

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, fer):
        self.__ferramenta = fer


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    def escrever(self, texto):
        print(f"Caneta está escrevendo: {texto}")


class MaquinaDeEscrever:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    def escrever(self, texto):
        print(f"Caneta está escrevendo: {texto}")
