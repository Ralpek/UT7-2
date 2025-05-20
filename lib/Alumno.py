class Alumno:
    def __init__(self, nie, nombre, apellidos, tramo='0', bilingue=False):
        self.nie = nie
        self.nombre = nombre
        self.apellidos = apellidos
        self.tramo = tramo
        self.bilingue = bilingue

    def __str__(self):
        return f"NIE: {self.nie}, Nombre: {self.nombre}, Apellidos: {self.apellidos}, Tramo: {self.tramo}, Bilingüe: {self.bilingue}"

    def __eq__(self, other):
        return isinstance(other, Alumno) and self.nie == other.nie

    def actualizar(self, nombre, apellidos, tramo, bilingue):
        self.nombre = nombre
        self.apellidos = apellidos
        self.tramo = tramo
        self.bilingue = bilingue
