from dataclass.Usuario import Usuario
class Usuarios:
    _usuarios = []
    def __len__(self):
        return len(self._usuarios)

    def __iter__(self):
        return iter(self._usuarios)

    def __getitem__(self, item):
        if 0 < item < len(self._usuarios):
            return self._usuarios[item]
        return None

    def append(self, other:Usuario):
        self._usuarios.append(other)

    def remove(self, index:int):
        if 0 < index < len(self._usuarios):
            del self._usuarios[index]

    def __str__(self):
        texto = ""
        for usuario in self._usuarios:
            texto += f"\t[{str(usuario)}],\n"
        return f"[\n{texto}]"
