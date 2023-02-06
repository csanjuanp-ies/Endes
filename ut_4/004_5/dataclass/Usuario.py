from datetime import datetime

class Usuario:
    TIPO = {
        'USUARIO' : 0,
        'ADMINISTRADOR' : 1,
    }

    _next_id :int = 0
    def __init__(self, nombre:str, direccion:str, fecha_ingreso:datetime):
        self._id:int = self._get_next_id()
        self.nombre:str = nombre
        self.direccion:str = direccion
        self.fecha_ingreso:datetime = fecha_ingreso
        self.fecha_cese:datetime|None = None
        self._tipo:Usuario.TIPO = Usuario.TIPO['USUARIO']

    def __str__(self):
        return f"({self._id}){self.nombre} [{self.direccion}] |{self.fecha_ingreso}|"

    def __eq__(self, other:"Usuario"):
        return self._id == other._id

    def _get_next_id(self):
        Usuario._next_id += 1
        return self._next_id

    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self, tipo):
        if tipo in Usuario.TIPO.keys():
            self._tipo = Usuario.TIPO[tipo]

    def get_usuario_array(self):
        return [self.nombre, self.direccion, self.fecha_ingreso]