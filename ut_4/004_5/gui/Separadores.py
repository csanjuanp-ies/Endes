class Separadores:
    ANCHO = 50
    @staticmethod
    def imprimir_separador():
        print("*" * Separadores.ANCHO)

    @staticmethod
    def imprimir_separador_secundario():
        print("-" * Separadores.ANCHO)
    @staticmethod
    def imprinmir_error(texto:str):
        print(("\033[1;31m" + texto + "\033[0m").center(Separadores.ANCHO))

    @staticmethod
    def imprinmir_texto(texto:str):
        print(("\033[1;36m" + texto + "\033[0m").center(Separadores.ANCHO))
