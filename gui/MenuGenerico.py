#from menu import Menu
from gestor.GestorCSV import GestorCSV

class MenuGenerico():
    def __init__(self, titulo, gestor_db, archivo_csv):
        self.titulo = titulo
        self.gestor = gestor_db
        self.csv_backup = GestorCSV(archivo_csv, gestor_db.tipo)

    def main(self):
        while True:
            self._visualizar_menu()
            opcion = self._recoger_opcion_menu()
            if not self._tratar_opcion_menu(opcion):
                break

    def _visualizar_menu(self):
        print(f"\n--- {self.titulo} ---")
        print("1. Crear")
        print("2. Mostrar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver al menú principal (y guardar respaldo CSV)")

    def _recoger_opcion_menu(self):
        try:
            return int(input("Seleccione una opción: "))
        except ValueError:
            return -1

    def _tratar_opcion_menu(self, opcion: int) -> bool:
        if opcion == 1:
            data = self._recoger_datos()
            self.gestor.crear(data)
        elif opcion == 2:
            self.gestor.cargar()
            for obj in self.gestor.objetos.values():
                print(obj)
        elif opcion == 3:
            key = input("Clave primaria: ")
            nuevos = self._recoger_datos()
            self.gestor.actualizar(key, nuevos)
        elif opcion == 4:
            key = input("Clave primaria: ")
            self.gestor.eliminar(key)
        elif opcion == 5:
            print("Guardando respaldo CSV...")
            self.csv_backup.guardar(self.gestor.objetos.values())
            return False
        else:
            print("Opción no válida.")
        return True

    def _recoger_datos(self):
        data = {}
        campos = self.gestor.tipo.__init__.__code__.co_varnames[1:self.gestor.tipo.__init__.__code__.co_argcount]
        for campo in campos:
            valor = input(f"{campo}: ")
            if campo == 'numero_ejemplares':
                valor = int(valor)
            if campo == 'bilingue':
                valor = valor.upper() == 'S'
            data[campo] = valor
        return data
