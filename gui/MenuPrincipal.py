from gui.MenuGenerico import MenuGenerico
from gestor.GestorDB import GestorDB
from gestor.GestorCSV import GestorCSV
from lib.Alumno import Alumno
from lib.Libro import Libro
from lib.Prestamo import Prestamo

class MenuPrincipal:
    def __init__(self, config):
        self.config = config
        self.gestores = {
            'alumnos': GestorDB(config['db_host'], config['db_user'], config['db_password'], config['db_name'], Alumno),
            'libros': GestorDB(config['db_host'], config['db_user'], config['db_password'], config['db_name'], Libro),
            'prestamos': GestorDB(config['db_host'], config['db_user'], config['db_password'], config['db_name'], Prestamo)
        }
        self.respaldos = {
            'alumnos': "alumnos.csv",
            'libros': "libros.csv",
            'prestamos': "prestamos.csv"
        }

    def mostrar(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Gestión de Alumnos")
            print("2. Gestión de Libros")
            print("3. Gestión de Préstamos")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                MenuGenerico("Alumnos", self.gestores['alumnos'], self.respaldos['alumnos']).main()
            elif opcion == '2':
                MenuGenerico("Libros", self.gestores['libros'], self.respaldos['libros']).main()
            elif opcion == '3':
                MenuGenerico("Préstamos", self.gestores['prestamos'], self.respaldos['prestamos']).main()
            elif opcion == '4':
                confirmar = input("\u00bfSeguro que desea salir? (S/N): ").strip().upper()
                if confirmar == 'S':
                    print("Saliendo del sistema...")
                    break
                else:
                    print("Cancelado.")
            else:
                print("Opción no válida. Intente de nuevo.")
