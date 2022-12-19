"""
Guardar un estado anterior al él y revertirlo si fuera necesario
"""


class ClaseGuardaEstado:
    estado = None
    estado_anterior = None

    def __init__(self, estado: int):
        self.estado = estado
        self.estado_anterior = estado

    def setEstado(self, estado: int):
        self.estado_anterior, self.estado = self.estado, estado

    def getEstado(self):
        return self.estado

    def revertirEstado(self):
        self.estado = self.estado_anterior

    def __str__(self):
        return "El estado actual es: %s, y el anterior: %s" % (self.estado, self.estado_anterior)


c = ClaseGuardaEstado(5)
print(c)
c.setEstado(6)
print(c)
c.setEstado(7)
print(c)
c.revertirEstado()
print(c)