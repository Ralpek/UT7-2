from abc import ABC, abstractmethod

class Menu(ABC):
    @abstractmethod
    def main(self):
        pass

    @abstractmethod
    def _tratar_opcion_menu(self, opcion: int) -> bool:
        pass

    @abstractmethod
    def _visualizar_menu(self):
        pass

    @abstractmethod
    def _recoger_opcion_menu(self) -> int:
        pass

class Objeto:
    def __init__(self, nombre=""):
        self.nombre = nombre

    def actualizar(self):
        self.nombre = input("Ingrese el nuevo nombre del objeto: ")
        print("Objeto actualizado correctamente.")

    def mostrar(self):
        if self.nombre:
            print(f"Objeto: {self.nombre}")
        else:
            print("No hay ningún objeto creado.")

    def eliminar(self):
        self.nombre = ""
        print("Objeto eliminado correctamente.")

class MenuConcreto(Menu):
    class OpcionesMenu:
        CREAR: int = 1
        MOSTRAR: int = 2
        ACTUALIZAR: int = 3
        ELIMINAR: int = 4
        SALIR: int = 5

        @staticmethod
        def opciones():
            return range(MenuConcreto.OpcionesMenu.CREAR, MenuConcreto.OpcionesMenu.SALIR + 1)

    def __init__(self):
        self.objeto = Objeto()

    def main(self):
        while True:
            self._visualizar_menu()
            opcion = self._recoger_opcion_menu()
            if not self._tratar_opcion_menu(opcion):
                break

    def _visualizar_menu(self):
        print("\nMenú de programación orientada a objetos:")
        print("1. Crear objeto")
        print("2. Mostrar objeto")
        print("3. Actualizar objeto")
        print("4. Eliminar objeto")
        print("5. Salir")

    def _recoger_opcion_menu(self) -> int:
        try:
            return int(input("Seleccione una opción: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            return -1

    def _tratar_opcion_menu(self, opcion: int) -> bool:
        if opcion == self.OpcionesMenu.CREAR:
            self.objeto.nombre = input("Ingrese el nombre del objeto: ")
            print("Objeto creado correctamente.")
        elif opcion == self.OpcionesMenu.MOSTRAR:
            self.objeto.mostrar()
        elif opcion == self.OpcionesMenu.ACTUALIZAR:
            self.objeto.actualizar()
        elif opcion == self.OpcionesMenu.ELIMINAR:
            self.objeto.eliminar()
        elif opcion == self.OpcionesMenu.SALIR:
            print("Saliendo del programa...")
            return False
        else:
            print("Opción no válida, intente de nuevo.")
        return True

if __name__ == "__main__":
    menu = MenuConcreto()
    menu.main()