import abc


class Fabrica:
    """
    Creación de una clase abstracta padre para gestionar varias hijas.
    Las hijas se define para qué tipo gestionan y la padre realiza la creación de forma adecuada
    """
    """
    Las variables que empiezan con __ se renombran en las clases hijas, por eso no se puede usar __valor
    """
    valor = None

    def __new__(cls, objeto):
        for clase in cls.__subclasses__():
            if clase.estaDiseñadaPara(objeto):
                o = object.__new__(clase)
                o.__init__(objeto)
                return o

    def __init__(self, objeto):
        self.valor = objeto

    @classmethod
    def estaDiseñadaPara(cls, objeto):
        if cls.tipo in str(type(objeto)):
            return True

    @abc.abstractmethod
    def __str__(self):
        pass


class GestionStr(Fabrica):
    tipo = "str"

    def __str__(self):
        return "Cadena: " + str(self.valor)


class GestionInt(Fabrica):
    tipo = "int"

    def __str__(self):
        return "Entero: " + str(self.valor)


miObjeto1 = Fabrica("Hola")
print(miObjeto1)            # Hola
miObjeto1 = Fabrica(23)
print(miObjeto1)            # 23
miObjeto1 = Fabrica(True)
print(miObjeto1)            # None

