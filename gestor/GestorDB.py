from configuracion import Archivo
import csv

class GestorDB:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = conexion.cursor()
        self._vaciar_tablas()
        self.cargar_datos()

    def _vaciar_tablas(self):
        self.cursor.execute("SET FOREIGN_KEY_CHECKS=0")
        for tabla in ["alumnoscrusoslibros", "libros", "alumnos", "cursos", "materias"]:
            self.cursor.execute(f"DELETE FROM {tabla}")
        self.cursor.execute("SET FOREIGN_KEY_CHECKS=1")
        self.conexion.commit()
        print("Tablas vaciadas correctamente.")

    def cerrar_conexion(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()

    def cargar_datos(self):
        def cargar_csv(ruta):
            with open(ruta, encoding='utf-8') as f:
                f.readline()
                reader = csv.reader(f, delimiter=',', quotechar='"')
                return [linea for linea in reader]

        def cargar_tabla(nombre_tabla, columnas, datos):
            self.cursor.execute(f"DELETE FROM {nombre_tabla}")
            for fila in datos:
                valores = ', '.join([f'"{campo}"' for campo in fila])
                sql = f"INSERT INTO {nombre_tabla} ({', '.join(columnas)}) VALUES ({valores})"
                self.cursor.execute(sql)

        # Cargar materias necesarias
        self.cursor.execute("INSERT IGNORE INTO materias (id, nombre, departamento) VALUES (1, 'Literatura', 'Lengua'), (2, 'Lengua', 'Lengua'), (3, 'Historia', 'Sociales')")

        # Cargar cursos necesarios
        self.cursor.execute("INSERT IGNORE INTO cursos (curso, nivel) VALUES ('1ESO', 'ESO'), ('2ESO', 'ESO'), ('3ESO', 'ESO')")

        cargar_tabla('alumnos', ['nie', 'nombre', 'apellidos', 'tramo', 'bilingue'], cargar_csv(Archivo.FILE_ALUMNOS))
        cargar_tabla('libros', ['isbn', 'titulo', 'autor', 'numero_ejemplares', 'id_materia', 'id_curso'], cargar_csv(Archivo.FILE_LIBROS))
        cargar_tabla('alumnoscrusoslibros', ['nie', 'curso', 'isbn', 'fecha_entrega', 'fecha_devolucion', 'estado'], cargar_csv(Archivo.FILE_PRESTAMOS))

        self.conexion.commit()
        print("Datos cargados correctamente desde CSV a la base de datos.")

    def guardar_consulta(self, datos, nombre_archivo="consulta.csv"):
        if not datos:
            print("No hay resultados para guardar.")
            return
        try:
            with open(nombre_archivo, "w", newline='', encoding="utf-8") as f:
                writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
                writer.writerows(datos)
            print(f"Resultado guardado en '{nombre_archivo}'.")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")


