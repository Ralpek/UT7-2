from gui.Menu import Menu
from gestor.GestorAlumnos import GestorAlumnos
from lib.Alumno import Alumno

class MenuAlumnos(Menu):
    def __init__(self, conexion, gestor_db):
        self.conexion = conexion
        self.gestor = GestorAlumnos(conexion)
        self.gestor_db = gestor_db
        self.resultado = []

    def main(self):
        while True:
            self._visualizar_menu()
            if not self._tratar_opcion_menu(self._recoger_opcion_menu()):
                break

    def _visualizar_menu(self):
        print("\n=== MENU ALUMNOS ===")
        print("1. Añadir alumno")
        print("2. Quitar alumno")
        print("3. Mostrar alumnos")
        print("4. Modificar alumno")
        print("5. Buscar por nombre o NIE")
        print("6. Guardar resultado de búsqueda")
        print("7. Volver")

    def _recoger_opcion_menu(self) -> int:
        try:
            return int(input("Seleccione una opción: "))
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")
            return -1

    def _tratar_opcion_menu(self, opcion: int) -> bool:
        if opcion == 1:
            nie = input("NIE: ")
            nombre = input("Nombre: ")
            apellidos = input("Apellidos: ")
            tramo = input("Tramo: ")
            bilingue = input("Bilingüe (S/N): ").strip().upper() == 'S'
            alumno = Alumno(nie, nombre, apellidos, tramo, bilingue)
            self.gestor.anadir(alumno)
            print("Alumno añadido correctamente.")

        elif opcion == 2:
            nie = input("Introduzca el NIE del alumno a eliminar: ")
            self.gestor.eliminar(nie)
            print("Alumno eliminado correctamente.")

        elif opcion == 3:
            self.resultado = self.gestor.mostrar()
            for a in self.resultado:
                print(a)

        elif opcion == 4:
            nie = input("NIE del alumno a modificar: ")
            campo = input("Campo a modificar (nombre, apellidos, tramo, bilingue): ")
            valor = input("Nuevo valor: ")
            if campo == "bilingue":
                valor = valor.upper() == 'S'
            self.gestor.modificar(nie, {campo: valor})
            print("Alumno modificado.")

        elif opcion == 5:
            criterio = input("Buscar por (NIE/NOMBRE): ").strip().lower()
            if criterio == 'nie':
                nie = input("Introduzca el NIE: ")
                self.resultado = self.gestor.buscar(nie=nie)
            elif criterio == 'nombre':
                nombre = input("Introduzca el nombre: ")
                self.resultado = self.gestor.buscar(nombre=nombre)
            else:
                print("Criterio inválido.")
                return True
            for r in self.resultado:
                print(r)

        elif opcion == 6:
            self.gestor_db.guardar_consulta(self.resultado, "consultaAlumnos.csv")

        elif opcion == 7:
            return False

        else:
            print("Opción no válida")
        return True