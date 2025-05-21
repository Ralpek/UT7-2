import mysql.connector
from mysql.connector import errorcode

class GestorDB:
    def __init__(self, host, user, password, database, tipo):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database
        }
        self.tipo = tipo
        self.conn = None
        self.cursor = None
        self.objetos = {}
        self.conectar()
        self.cargar()

    def conectar(self):
        try:
            self.conn = mysql.connector.connect(**self.config)
            self.conn.autocommit = True
            self.cursor = self.conn.cursor(dictionary=True)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de acceso a la base de datos")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("La base de datos no existe")
            else:
                print(err)

    def cerrar(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def cargar(self):
        tabla = self.tipo.__name__.lower() + 's'
        self.objetos = {}
        try:
            self.cursor.execute(f"SELECT * FROM {tabla}")
            for row in self.cursor.fetchall():
                key = f"{row['nie']}_{row['isbn']}" if self.tipo.__name__ == "Prestamo" else row.get('nie', row.get('isbn'))
                if 'numero_ejemplares' in row:
                    row['numero_ejemplares'] = int(row['numero_ejemplares'])
                if 'bilingue' in row:
                    row['bilingue'] = row['bilingue'] in ['1', 1, True, 'True']
                self.objetos[key] = self.tipo(**row)
        except mysql.connector.Error as err:
            print(f"Error al cargar: {err}")

    def crear(self, data):
        key = f"{data['nie']}_{data['isbn']}" if self.tipo.__name__ == "Prestamo" else data.get('nie', data.get('isbn'))
        if key in self.objetos:
            print("Ya existe.")
            return
        self.objetos[key] = self.tipo(**data)
        campos = ', '.join(data.keys())
        valores = ', '.join(['%s'] * len(data))
        sql = f"INSERT INTO {self.tipo.__name__.lower()}s ({campos}) VALUES ({valores})"
        try:
            self.cursor.execute(sql, tuple(data.values()))
            print("Creado correctamente.")
        except mysql.connector.Error as err:
            print(f"Error al insertar: {err}")

    def actualizar(self, key, nuevos_datos):
        if key not in self.objetos:
            print("No encontrado.")
            return
        self.objetos[key].__init__(**nuevos_datos)
        sets = ', '.join([f"{campo}=%s" for campo in nuevos_datos])
        if self.tipo.__name__ == "Prestamo":
            where = "nie=%s AND isbn=%s"
            claves = key.split('_')
        else:
            pk = 'nie' if 'nie' in nuevos_datos else 'isbn'
            where = f"{pk}=%s"
            claves = [key]
        sql = f"UPDATE {self.tipo.__name__.lower()}s SET {sets} WHERE {where}"
        try:
            self.cursor.execute(sql, tuple(nuevos_datos.values()) + tuple(claves))
            print("Actualizado correctamente.")
        except mysql.connector.Error as err:
            print(f"Error al actualizar: {err}")

    def eliminar(self, key):
        if key not in self.objetos:
            print("No encontrado.")
            return
        if self.tipo.__name__ == "Prestamo":
            sql = f"DELETE FROM prestamos WHERE nie=%s AND isbn=%s"
            claves = key.split('_')
        else:
            pk = 'nie' if self.tipo.__name__ == 'Alumno' else 'isbn'
            sql = f"DELETE FROM {self.tipo.__name__.lower()}s WHERE {pk}=%s"
            claves = [key]
        try:
            self.cursor.execute(sql, tuple(claves))
            del self.objetos[key]
            print("Eliminado correctamente.")
        except mysql.connector.Error as err:
            print(f"Error al eliminar: {err}")
