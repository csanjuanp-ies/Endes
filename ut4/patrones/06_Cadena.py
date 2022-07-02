"""
Patrón cadena   c1(m1) -> c2 -> c3
"""
import abc


class Interfaz:
    __metaclass__ = abc.ABCMeta

    _next = None

    def next(self, n):
        if isinstance(n, Interfaz):
            self._next = n

    @abc.abstractmethod
    def run(self, msg): pass


class MiClase1(Interfaz):
    def run(self, msg):
        print("1.-" + msg)
        if self._next is not None:
            self._next.run(msg)


class MiClase2(Interfaz):
    def run(self, msg):
        print("2.-" + msg)
        if self._next is not None:
            self._next.run(msg)


c1 = MiClase1()
c2 = MiClase2()
c3 = MiClase2()
c1.next(c2)
c2.next(c3)
c1.run("Hola")
