import csv

class GestorCSV:
    def __init__(self, archivo, tipo):
        self.archivo = archivo
        self.tipo = tipo
        self.objetos = {}
        self._cargar_desde_csv()

    def crear(self):
        data = self._recoger_datos()
        key = self._clave_primaria(data)
        if key in self.objetos:
            print("Ya existe.")
            return
        self.objetos[key] = self.tipo(**data)
        print("Objeto creado.")

    def mostrar(self):
        for obj in self.objetos.values():
            print(obj)

    def actualizar(self):
        key = input("Clave primaria: ")
        if key in self.objetos:
            nuevos = self._recoger_datos()
            self.objetos[key].__init__(**nuevos)
            print("Actualizado.")
        else:
            print("No existe.")

    def eliminar(self):
        key = input("Clave primaria: ")
        if key in self.objetos:
            del self.objetos[key]
            print("Eliminado.")
        else:
            print("No encontrado.")

    def guardar(self):
        campos = self.tipo.__init__.__code__.co_varnames[1:self.tipo.__init__.__code__.co_argcount]
        with open(self.archivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=campos, delimiter=';')
            writer.writeheader()
            for obj in self.objetos.values():
                writer.writerow({campo: getattr(obj, campo) for campo in campos})

    def _cargar_desde_csv(self):
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f, delimiter=';')
                for row in reader:
                    if 'numero_ejemplares' in row:
                        row['numero_ejemplares'] = int(row['numero_ejemplares'])
                    if 'bilingue' in row:
                        row['bilingue'] = row['bilingue'] == 'True'
                    key = self._clave_primaria(row)
                    self.objetos[key] = self.tipo(**row)
        except FileNotFoundError:
            pass

    def _clave_primaria(self, datos):
        return f"{datos['nie']}_{datos['isbn']}" if self.tipo.__name__ == "Prestamo" else datos.get('nie', datos.get('isbn'))

    def _recoger_datos(self):
        data = {}
        for campo in self.tipo.__init__.__code__.co_varnames[1:self.tipo.__init__.__code__.co_argcount]:
            valor = input(f"{campo}: ")
            if campo == 'numero_ejemplares':
                valor = int(valor)
            if campo == 'bilingue':
                valor = valor.upper() == 'S'
            data[campo] = valor
        return data
