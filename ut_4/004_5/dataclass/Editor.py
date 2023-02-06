class Editor:
    _next_id:int = 0

    def __init__(self, nombre:str, direccion:str):
        self._id = self._get_next_id()
        self.nombre:str = nombre
        self.direccion:str = direccion

    def __str__(self):
        return f"({self._id}){self.nombre} [{self.direccion}]"

    def __eq__(self, other:"Editor"):
        return self._id == other._id

    def _get_next_id(self):
        Editor._next_id += 1
        return self._next_id

    def get_editor_array(self):
        return [self.nombre, self.direccion]