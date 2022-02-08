from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def falar(self, msg):
        print(f"{self.__class__.__name__} está falando {msg}")


class B(A):
    def falar(self, msg):
        super().falar(msg)


class C(A):
    def falar(self, msg):
        super().falar(msg)


b = B()
c = C()

b.falar("a")
c.falar("b")
