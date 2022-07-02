class Singleton:
    """
    Este patrón es para mantener un único objeto pero con varias referencias.
    """
    __instance = None
    __value = 0

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __str__(self):
        return "Mi Objeto: " + str(self.__value)

    def setvalue(self, val: int):
        self.__value = val

    @classmethod
    def me(cls):
        return cls.__instance


miObjeto1 = Singleton()
print(miObjeto1)        # 0
miObjeto2 = Singleton()
miObjeto2.setvalue(5)
print(miObjeto1)        # 5
print(Singleton.me())   # 5
