class Alumno:
    def __init__(self, nie: str, nombre: str, apellidos: str, tramo: str, bilingue: bool):
        self.nie = nie
        self.nombre = nombre
        self.apellidos = apellidos
        self.tramo = tramo
        self.bilingue = bilingue

    def __str__(self):
        return f"{self.nie} - {self.nombre} {self.apellidos}, Tramo: {self.tramo}, Bilingüe: {self.bilingue}"

    def __eq__(self, other):
        return isinstance(other, Alumno) and self.nie == other.nie
