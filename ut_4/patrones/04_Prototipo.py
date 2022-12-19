from copy import deepcopy

class Prototipo:
    """
    Cuando una instanciación es compleja es mejor hacer una copia de uno ya existente
    """
    _instancia_primera = None

    def __new__(cls):
        result = object.__new__(cls)
        if cls._instancia_primera is not None:
            result.__dict__ = deepcopy(cls._instancia_primera.__dict__)
        else:
            cls._instancia_primera = result
        return result

    def __init__(self):
        if self._instancia_primera is not None:
            self._instancia_primera = None
            self.x = 0
            self.y = 0

    def __str__(self):
        return "(%s,%s)" % (self.x, self.y)


miObjeto1 = Prototipo()     #miObjeto1 será el referente para todos los demás
miObjeto1.x = 1
print(miObjeto1)            # (1,0)
miObjeto2 = Prototipo()
miObjeto2.y = 3
print(miObjeto2)            # (1,3)
miObjeto1.x = 2             # cambio el referente
miObjeto3 = Prototipo()
print(miObjeto3)            # (2,0)