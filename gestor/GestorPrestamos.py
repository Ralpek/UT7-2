class GestorPrestamos:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = conexion.cursor()

    def anadir(self, prestamo):
        sql = """
        INSERT INTO alumnoscrusoslibros (nie, curso, isbn, fecha_entrega, fecha_devolucion, estado)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        datos = (
            prestamo.nie,
            prestamo.id_curso,
            prestamo.isbn,
            prestamo.fecha_entrega,
            prestamo.fecha_devolucion,
            'D' if prestamo.estado else 'P'
        )
        self.cursor.execute(sql, datos)
        self.conexion.commit()

    def mostrar(self):
        self.cursor.execute("SELECT * FROM alumnoscrusoslibros")
        return self.cursor.fetchall()

    def buscar(self, nie=None, curso=None, isbn=None, fecha_entrega=None, fecha_devolucion=None, estado=None):
        condiciones = []
        valores = []
        if nie:
            condiciones.append("nie = %s")
            valores.append(nie)
        if curso:
            condiciones.append("curso = %s")
            valores.append(curso)
        if isbn:
            condiciones.append("isbn = %s")
            valores.append(isbn)
        if fecha_entrega:
            condiciones.append("fecha_entrega = %s")
            valores.append(fecha_entrega)
        if fecha_devolucion:
            condiciones.append("fecha_devolucion = %s")
            valores.append(fecha_devolucion)
        if estado:
            condiciones.append("nie = %s")
            valores.append(nie)

        if not condiciones:
            return []

        sql = f"SELECT * FROM alumnoscrusoslibros WHERE {' AND '.join(condiciones)}"
        self.cursor.execute(sql, tuple(valores))
        return self.cursor.fetchall()

    def eliminar(self, nie, curso, isbn):
        self.cursor.execute(
            "DELETE FROM alumnoscrusoslibros WHERE nie = %s AND curso = %s AND isbn = %s",
            (nie, curso, isbn)
        )
        self.conexion.commit()
