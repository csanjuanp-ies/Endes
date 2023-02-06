from dataclass.Libro import Libro
class Libros:
    _libros = []
    def __len__(self):
        return len(self._libros)

    def __iter__(self):
        return iter(self._libros)

    def __getitem__(self, item):
        if 0 < item < len(self._libros):
            return self._libros[item]
        return None

    def append(self, other:Libro):
        self._libros.append(other)

    def remove(self, index:int):
        if 0 < index < len(self._libros):
            del self._libros[index]

    def __str__(self):
        texto = ""
        for editor in self._libros:
            texto += f"\t[{str(editor)}],\n"
        return f"[\n{texto}]"
