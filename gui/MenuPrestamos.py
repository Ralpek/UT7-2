from gui.Menu import Menu
from gestor.GestorPrestamos import GestorPrestamos
from lib.Prestamo import Prestamo
from datetime import datetime

class MenuPrestamos(Menu):
    def __init__(self, conexion, gestor_db):
        self.conexion = conexion
        self.gestor = GestorPrestamos(conexion)
        self.gestor_db = gestor_db
        self.resultado = []

    def main(self):
        while True:
            self._visualizar_menu()
            if not self._tratar_opcion_menu(self._recoger_opcion_menu()):
                break

    def _visualizar_menu(self):
        print("\n=== MENU PRÉSTAMOS ===")
        print("1. Añadir préstamo")
        print("2. Quitar préstamo")
        print("3. Mostrar préstamos")
        print("4. Buscar por NIE, curso, ISBN, fecha de entrega/devolución o estado")
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
            nie = input("NIE: ")
            id_curso = input("Curso: ")
            isbn = input("ISBN: ")
            fecha_entrega = input("Fecha de entrega (YYYY-MM-DD): ")
            fecha_devolucion = input("Fecha de devolución (YYYY-MM-DD): ")
            estado = input("Estado (D para Devuelto, P para Prestado): ").strip().upper() == 'D'
            prestamo = Prestamo(
                nie,
                id_curso,
                isbn,
                datetime.strptime(fecha_entrega, "%Y-%m-%d").date(),
                datetime.strptime(fecha_devolucion, "%Y-%m-%d").date(),
                estado
            )
            self.gestor.anadir(prestamo)
            print("Préstamo registrado correctamente.")

        elif opcion == 2:
            nie = input("NIE del préstamo a eliminar: ")
            curso = input("Curso: ")
            isbn = input("ISBN: ")
            self.gestor.eliminar(nie, curso, isbn)
            print("Préstamo eliminado correctamente.")

        elif opcion == 3:
            self.resultado = self.gestor.mostrar()
            for p in self.resultado:
                print(p)

        elif opcion == 4:
            nie = input("NIE (opcional): ") or None
            curso = input("Curso (opcional): ") or None
            isbn = input("ISBN (opcional): ") or None
            fecha_entrega = input("Fecha entrega (YYYY-MM-DD, opcional): ") or None
            fecha_devolucion = input("Fecha devolución (YYYY-MM-DD, opcional): ") or None
            estado = input("Estado (opcional): ") or None

            if fecha_entrega:
                fecha_entrega = datetime.strptime(fecha_entrega, "%Y-%m-%d").date()
            if fecha_devolucion:
                fecha_devolucion = datetime.strptime(fecha_devolucion, "%Y-%m-%d").date()

            self.resultado = self.gestor.buscar(
                nie=nie,
                curso=curso,
                isbn=isbn,
                fecha_entrega=fecha_entrega,
                fecha_devolucion=fecha_devolucion,
                estado=estado
            )
            for r in self.resultado:
                print(r)

        elif opcion == 5:
            self.gestor_db.guardar_consulta(self.resultado, "consultaPrestamos.csv")

        elif opcion == 6:
            return False

        else:
            print("Opción no válida.")
        return True
