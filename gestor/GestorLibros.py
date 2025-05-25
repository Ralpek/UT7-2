class GestorLibros:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = conexion.cursor()

    def anadir(self, libro):
        sql = """
        INSERT INTO libros (isbn, titulo, autor, numero_ejemplares, id_materia, id_curso)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        datos = (libro.isbn, libro.titulo, libro.autor, libro.numero_ejemplares, libro.id_materia, libro.id_curso)
        self.cursor.execute(sql, datos)
        self.conexion.commit()

    def mostrar(self):
        self.cursor.execute("SELECT * FROM libros")
        return self.cursor.fetchall()

    def buscar(self, isbn=None, titulo=None):
        if isbn:
            self.cursor.execute("SELECT * FROM libros WHERE isbn = %s", (isbn,))
        elif titulo:
            self.cursor.execute("SELECT * FROM libros WHERE titulo LIKE %s", (f"%{titulo}%",))
        else:
            return []
        return self.cursor.fetchall()

    def modificar(self, isbn, nuevos_datos):
        campos = []
        valores = []
        for campo, valor in nuevos_datos.items():
            campos.append(f"{campo} = %s")
            valores.append(valor)
        valores.append(isbn)
        sql = f"UPDATE libros SET {', '.join(campos)} WHERE isbn = %s"
        self.cursor.execute(sql, tuple(valores))
        self.conexion.commit()
