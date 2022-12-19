"""
Un objeto es observado por varios, y son notificados cuando cambia
"""
import abc


class Observador(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self, msg):
        pass

    @abc.abstractmethod
    def update(self, msg):
        pass


class Observado:
    _lista_observadores = []
    _valor = None

    def __init__(self, valor: int):
        self._valor = valor

    def setObservador(self, obs: Observador):
        self._lista_observadores.append(obs)

    def removeObservador(self, obs: Observador):
        self._lista_observadores.remove(obs)

    def notify(self):
        for ele in self._lista_observadores:
            ele.update(self._valor)

    def setValor(self, valor: int):
        self._valor = valor
        self.notify()


class Punto(Observador):
    def __init__(self, msg):
        self.msg = msg

    def run(self, msg):
        print("Punto %s: %s" % (self.msg, msg))

    def update(self, msg):
        super().update(msg)
        self.run(msg)


obs = Observado(4)
obs1 = Punto("Uno")
obs2 = Punto("Dos")
obs.setObservador(obs1)
obs.setObservador(obs2)
obs.setValor(5)
obs.removeObservador(obs1)
obs.setValor(6)
