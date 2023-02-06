from dataclass.Prestamo import Prestamo
class Prestamos:
    _prestamos = []
    def __len__(self):
        return len(self._prestamos)

    def __iter__(self):
        return iter(self._prestamos)

    def __getitem__(self, item):
        if 0 < item < len(self._prestamos):
            return self._prestamos[item]
        return None

    def append(self, other:Prestamo):
        self._prestamos.append(other)

    def remove(self, index:int):
        if 0 < index < len(self._prestamos):
            del self._prestamos[index]

    def __str__(self):
        texto = ""
        for prestamo in self._prestamos:
            texto += f"\t[{str(prestamo)}],\n"
        return f"[\n{texto}]"
