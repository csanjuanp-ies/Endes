import abc
"""
El uso de objetos no generados por nosotros, los tenemos que adaptar a nuestro uso mediante
una clase que hace dicha adaptación
"""

# clase generadas por otros


class Perro:
    def ladrar(self):
        return "Ladrando..."


class Gato:
    def maullar(self):
        return "Maullando..."


"""
Queremos hacer uso de las clases anteriores en nuestra aplicación pero de una forma similar ambas
"""


class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def hacer_ruido(self):
        pass


class AdaptadorPerro(Animal, Perro):
    def hacer_ruido(self):
        return self.ladrar()


class AdaptadorGato(Animal, Gato):
    def hacer_ruido(self):
        return self.maullar()


for inx in [AdaptadorPerro(), AdaptadorGato()]:
    print(inx.hacer_ruido())


"""
La solución anterior funciona, pero no tiene el espíritu del patrón en el que debe guardarse la referencia al objeto
original
"""


class AdaptadorPerro(Animal):
    def __init__(self, objeto: Perro):
        self._obj = objeto

    def hacer_ruido(self):
        return self._obj.ladrar()

    def __getattr__(self, item):
        return self._obj.__getattribute__(item)


class AdaptadorGato(Animal):
    def __init__(self, objeto: Gato):
        self._obj = objeto

    def hacer_ruido(self):
        return self.maullar()

    def __getattr__(self, item):
        return self._obj.__getattribute__(item)


for inx in [AdaptadorPerro(Perro()), AdaptadorGato(Gato())]:
    print(inx.hacer_ruido())


"""
Mejor todavía si usamos una factoría
"""

class Factoria:
    @classmethod
    def getAnimal(cls, obj):
        if isinstance(obj, Perro): return AdaptadorPerro(obj)
        if isinstance(obj, Gato): return AdaptadorGato(obj)
        return None

for inx in [Perro(), Perro(), Gato()]:
    print(Factoria.getAnimal(inx).hacer_ruido())

