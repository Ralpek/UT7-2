from gui.Menu import Menu
from gestor.GestorDB import GestorDB

class MenuPrincipal(Menu):
    def __init__(self, menu_alumnos, menu_prestamos, menu_libros, conexion):
        self.menu_alumnos = menu_alumnos
        self.menu_prestamos = menu_prestamos
        self.menu_libros = menu_libros
        self.conexion = conexion
        self.gestor_db = GestorDB(conexion)

    def main(self):
        while True:
            self._visualizar_menu()
            if not self._tratar_opcion_menu(self._recoger_opcion_menu()):
                break

    def _visualizar_menu(self):
        print("\n=== MENU PRINCIPAL ===")
        print("1. Menú Alumnos")
        print("2. Menú Libros")
        print("3. Menú Préstamos")
        print("4. Salir")

    def _recoger_opcion_menu(self) -> int:
        try:
            return int(input("Seleccione una opción: "))
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")
            return -1

    def _tratar_opcion_menu(self, opcion: int) -> bool:
        if opcion == 1:
            self.menu_alumnos.main()
        elif opcion == 2:
            self.menu_libros.main()
        elif opcion == 3:
            self.menu_prestamos.main()
        elif opcion == 4:
            confirm = input("¿Seguro que desea salir? (S/N): ").strip().upper()
            return confirm != 'S'
        else:
            print("Opción no válida.")
        return True