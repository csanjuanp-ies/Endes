from dataclass.Editor import Editor
class Editores:
    _editores = []
    def __len__(self):
        return len(self._editores)

    def __iter__(self):
        return iter(self._editores)

    def __getitem__(self, item):
        if 0 < item < len(self._editores):
            return self._editores[item]
        return None

    def append(self, other:Editor):
        self._editores.append(other)

    def remove(self, index:int):
        if 0 < index < len(self._editores):
            del self._editores[index]

    def __str__(self):
        texto = ""
        for editor in self._editores:
            texto += f"\t[{str(editor)}],\n"
        return f"[\n{texto}]"
