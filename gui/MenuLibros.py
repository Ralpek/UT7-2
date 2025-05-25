from gui.Menu import Menu
from gestor.GestorLibros import GestorLibros
from lib.Libro import Libro

class MenuLibros(Menu):
    def __init__(self, conexion, gestor_db):
        self.conexion = conexion
        self.gestor = GestorLibros(conexion)
        self.gestor_db = gestor_db
        self.resultado = []

    def main(self):
        while True:
            self._visualizar_menu()
            if not self._tratar_opcion_menu(self._recoger_opcion_menu()):
                break

    def _visualizar_menu(self):
        print("\n=== MENU LIBROS ===")
        print("1. Añadir libro")
        print("2. Quitar libro")
        print("3. Mostrar libros")
        print("4. Buscar por nombre o ISBN")
        print("5. Guardar resultado de búsqueda")
        print("6. Volver")

    def _recoger_opcion_menu(self) -> int:
        try:
            return int(input("Seleccione una opción: "))
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")
            return -1

    def _tratar_opcion_menu(self, opcion: int) -> bool:
        if opcion == 1:
            isbn = input("ISBN: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            numero_ejemplares = int(input("Nº de ejemplares: "))
            id_materia = int(input("ID Materia: "))
            id_curso = input("ID Curso: ")
            libro = Libro(isbn, titulo, autor, numero_ejemplares, id_materia, id_curso)
            self.gestor.anadir(libro)
            print("Libro añadido correctamente.")

        elif opcion == 2:
            print("[Quitar libro] - (lógica pendiente)")

        elif opcion == 3:
            self.resultado = self.gestor.mostrar()
            for l in self.resultado:
                print(l)

        elif opcion == 4:
            criterio = input("Buscar por (ISBN/TITULO): ").strip().lower()
            if criterio == 'isbn':
                isbn = input("Introduzca el ISBN: ")
                self.resultado = self.gestor.buscar(isbn=isbn)
            elif criterio == 'titulo':
                titulo = input("Introduzca el título: ")
                self.resultado = self.gestor.buscar(titulo=titulo)
            else:
                print("Criterio inválido.")
                return True
            for r in self.resultado:
                print(r)

        elif opcion == 5:
            self.gestor_db.guardar_consulta(self.resultado, "consultaLibros.csv")

        elif opcion == 6:
            return False

        else:
            print("Opción no válida.")
        return True

