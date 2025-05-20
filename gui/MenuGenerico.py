from menu import Menu

class MenuGenerico(Menu):
    def __init__(self, titulo, gestor):
        self.titulo = titulo
        self.gestor = gestor

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
        print("5. Guardar")
        print("6. Volver al menú principal")

    def _recoger_opcion_menu(self):
        try:
            return int(input("Seleccione una opción: "))
        except ValueError:
            return -1

    def _tratar_opcion_menu(self, opcion: int) -> bool:
        acciones = {
            1: self.gestor.crear,
            2: self.gestor.mostrar,
            3: self.gestor.actualizar,
            4: self.gestor.eliminar,
            5: self.gestor.guardar
        }
        if opcion == 6:
            self.gestor.guardar()
            return False
        accion = acciones.get(opcion)
        if accion:
            accion()
        else:
            print("Opción no válida.")
        return True
