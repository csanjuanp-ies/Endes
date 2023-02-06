from dataclass.Editor import Editor
class Libro:
    _next_id:int = 0
    def __init__(self, autor:str, titulo:str, precio:int):
        self._id = self._get_next_id()
        self.autor:str = autor
        self.titulo:str = titulo
        self.precio:int = precio
        self.disponible = True
        self._publicado_por = None

    def __str__(self):
        return f"({self._id}){self.autor} [{self.titulo}|{self.precio}|]"

    def __eq__(self, other):
        if isinstance(other, Libro):
            return self._id == other._id
        elif isinstance(other, int):
            return self._id == other
    def _get_next_id(self):
        Libro._next_id += 1
        return self._next_id

    @property
    def publicado_por(self):
        return self._publicado_por

    @publicado_por.setter
    def publicado_por(self, valor:Editor):
        if isinstance(valor, Editor):
            self._publicado_por = valor

    def get_libro_array(self):
        return [self.autor,
                self.titulo,
                self.precio,
                self.disponible,
                self._publicado_por.nombre if self.publicado_por else None]
