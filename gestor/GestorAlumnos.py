class GestorAlumnos:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = conexion.cursor()

    def anadir(self, alumno):
        sql = """
        INSERT INTO alumnos (nie, nombre, apellidos, tramo, bilingue)
        VALUES (%s, %s, %s, %s, %s)
        """
        datos = (alumno.nie, alumno.nombre, alumno.apellidos, alumno.tramo, int(alumno.bilingue))
        self.cursor.execute(sql, datos)
        self.conexion.commit()

    def mostrar(self):
        self.cursor.execute("SELECT * FROM alumnos")
        return self.cursor.fetchall()

    def buscar(self, nie=None, nombre=None):
        if nie:
            self.cursor.execute("SELECT * FROM alumnos WHERE nie = %s", (nie,))
        elif nombre:
            self.cursor.execute("SELECT * FROM alumnos WHERE nombre LIKE %s", (f"%{nombre}%",))
        else:
            return []
        return self.cursor.fetchall()

    def modificar(self, nie, nuevos_datos):
        campos = []
        valores = []
        for campo, valor in nuevos_datos.items():
            campos.append(f"{campo} = %s")
            valores.append(valor)
        valores.append(nie)
        sql = f"UPDATE alumnos SET {', '.join(campos)} WHERE nie = %s"
        self.cursor.execute(sql, tuple(valores))
        self.conexion.commit()

    def eliminar(self, nie):
        self.cursor.execute("DELETE FROM alumnoscrusoslibros WHERE nie = %s", (nie,))
        self.cursor.execute("DELETE FROM alumnos WHERE nie = %s", (nie,))
        self.conexion.commit()
