import abc


class FiguraGeometrica:
    """
    Sería mucho mejor usar propiedades y setter
    """
    numero_lados = 0
    longitud = 0
    radio = 0

    def __str__(self):
        return "Numero de lados: %s, la longitud %s u el radio: %s" % (self.numero_lados, self.longitud, self.radio)


class Constructor:
    def __init__(self):
        self._producto = None

    @property
    def producto(self):
        return self._producto

    @producto.setter
    def producto(self, prod: FiguraGeometrica):
        self._producto = prod

    def crearProducto(self):
        self._producto = FiguraGeometrica()

    @abc.abstractmethod
    def configurarNumeroLados(self):
        pass

    @abc.abstractmethod
    def configurarLongitud(self):
        pass

    @abc.abstractmethod
    def configurarRadio(self):
        pass


class Cubo(Constructor):
    def configurarNumeroLados(self):
        self.producto.numero_lados = 4

    def configurarLongitud(self):
        self.producto.longitud = 20

    def configurarRadio(self):
        pass


class Triangulo(Constructor):
    def configurarNumeroLados(self):
        self.producto.numero_lados = 3

    def configurarLongitud(self):
        self.producto.longitud = 15

    def configurarRadio(self):
        pass


class Circunferencia(Constructor):
    def configurarNumeroLados(self):
        pass

    def configurarLongitud(self):
        pass

    def configurarRadio(self):
        self.producto.radio = 10


class Director:
    """
    Cuando una clase es muy compleja de inicializar, en vez de proporcionar métodos diferentes para cada tipo
    de inicialización, se crean constructores diferentes para cada tipo
    """
    def __init__(self):
        self._constructor = None

    @property
    def constructor(self):
        return self._constructor

    @constructor.setter
    def constructor(self, construct: Constructor):
        self._constructor = construct

    def crearProducto(self):
        self.constructor.crearProducto()
        self.constructor.configurarLongitud()
        self.constructor.configurarNumeroLados()
        self.constructor.configurarRadio()
        return self.constructor.producto


direcc = Director()
direcc.constructor = Cubo()
producto = direcc.crearProducto()
print(producto)
direcc.constructor = Triangulo()
producto = direcc.crearProducto()
print(producto)
direcc.constructor = Circunferencia()
producto = direcc.crearProducto()
print(producto)
