from gui.MenuLogin import MenuLogin
from gui.MenuPrincipal import MenuPrincipal
from gui.MenuAlumnos import MenuAlumnos
from gui.MenuLibros import MenuLibros
from gui.MenuPrestamos import MenuPrestamos
from gestor.GestorDB import GestorDB
from configuracion import Conectar_BBDD
import mysql.connector

def main():
    login = MenuLogin()
    if login.main() is None:
        conexion = mysql.connector.connect(
            user=Conectar_BBDD.USER,
            password=Conectar_BBDD.PASSWORD,
            host=Conectar_BBDD.HOST,
            database=Conectar_BBDD.DATABASE
        )

        gestor_db = GestorDB(conexion)

        menu_alumnos = MenuAlumnos(conexion, gestor_db)
        menu_libros = MenuLibros(conexion, gestor_db)
        menu_prestamos = MenuPrestamos(conexion, gestor_db)

        principal = MenuPrincipal(menu_alumnos, menu_prestamos, menu_libros, conexion)
        principal.main()

if __name__ == "__main__":
    main()


