import csv

class GestorCSV:
    def __init__(self, archivo, tipo):
        self.archivo = archivo
        self.tipo = tipo
        self.objetos = {}
        self._cargar()

    def crear(self):
        data = self._recoger_datos()
        key = f"{data['nie']}_{data['isbn']}" if self.tipo.__name__ == "Prestamo" else data.get('nie', data.get('isbn'))
        if key in self.objetos:
            print("El objeto ya existe o el préstamo está duplicado.")
            return
        self.objetos[key] = self.tipo(**data)
        print("Creado correctamente.")

    def mostrar(self):
        if not self.objetos:
            print("No hay datos.")
            return
        for obj in self.objetos.values():
            print(obj)

    def actualizar(self):
        key = input("Ingrese la clave primaria (NIE, ISBN o NIE_ISBN): ")
        obj = self.objetos.get(key)
        if obj:
            nuevos_datos = self._recoger_datos()
            obj.__init__(**nuevos_datos)
            print("Actualizado correctamente.")
        else:
            print("No encontrado.")

    def eliminar(self):
        key = input("Ingrese la clave primaria (NIE, ISBN o NIE_ISBN): ")
        if key in self.objetos:
            del self.objetos[key]
            print("Eliminado correctamente.")
        else:
            print("No encontrado.")

    def guardar(self):
        with open(self.archivo, 'w', newline='', encoding='utf-8') as f:
            campos = self.tipo.__init__.__code__.co_varnames[1:self.tipo.__init__.__code__.co_argcount]
            writer = csv.DictWriter(f, fieldnames=campos, delimiter=';')
            writer.writeheader()
            for obj in self.objetos.values():
                writer.writerow({campo: getattr(obj, campo) for campo in campos})

    def _cargar(self):
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f, delimiter=';')
                for row in reader:
                    if 'numero_ejemplares' in row:
                        row['numero_ejemplares'] = int(row['numero_ejemplares'])
                    if 'bilingue' in row:
                        row['bilingue'] = row['bilingue'] == 'True'
                    key = f"{row['nie']}_{row['isbn']}" if self.tipo.__name__ == "Prestamo" else row.get('nie', row.get('isbn'))
                    self.objetos[key] = self.tipo(**row)
        except FileNotFoundError:
            pass

    def _recoger_datos(self):
        data = {}
        campos = self.tipo.__init__.__code__.co_varnames[1:self.tipo.__init__.__code__.co_argcount]
        for campo in campos:
            valor = input(f"{campo}: ")
            if campo == 'numero_ejemplares':
                valor = int(valor)
            if campo == 'bilingue':
                valor = valor.upper() == 'S'
            data[campo] = valor
        return data