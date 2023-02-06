from almacenes.Libreria import Libreria
class App:
    @staticmethod
    def main():
        libreria = Libreria()
        libreria.cargar_usuarios()
        libreria.cargar_editores()
        libreria.cargar_libros()
        print(libreria)

App.main()
