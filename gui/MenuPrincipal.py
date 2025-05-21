from menu import Menu
from MenuGenerico import MenuGenerico
from lib.Alumno import Alumno
from lib.Libro import Libro
from lib.Prestamo import Prestamo
from login import Login
from gestor.GestorCSV import GestorCSV

CSV_ALUMNOS = "alumnos.csv"
CSV_LIBROS = "libros.csv"
CSV_PRESTAMOS = "prestamos.csv"

class MenuPrincipal:
    def __init__(self):
        self.login = Login("config.txt")

    def mostrar(self):
        if not self.login.autenticar():
            print("Autenticación fallida. Saliendo...")
            return

        while True:
            print("\nMenú Principal")
            print("1. Menú Alumnos")
            print("2. Menú Libros")
            print("3. Menú Préstamos")
            print("4. Salir")
            seleccion = input("Seleccione un menú: ")

            if seleccion == '1':
                MenuGenerico("Gestión de Alumnos", GestorCSV(CSV_ALUMNOS, Alumno)).main()
            elif seleccion == '2':
                MenuGenerico("Gestión de Libros", GestorCSV(CSV_LIBROS, Libro)).main()
            elif seleccion == '3':
                MenuGenerico("Gestión de Préstamos", GestorCSV(CSV_PRESTAMOS, Prestamo)).main()
            elif seleccion == '4':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida.")

#if __name__ == '__main__':
#    MenuPrincipal().mostrar()