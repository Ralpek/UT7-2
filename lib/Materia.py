class Materia:
    def __init__(self, id_materia: int, nombre: str, departamento: str):
        self.id_materia = id_materia
        self.nombre = nombre
        self.departamento = departamento

    def __str__(self):
        return f"{self.nombre} ({self.id_materia}) - Departamento: {self.departamento}"

    def __eq__(self, other):
        return isinstance(other, Materia) and self.id_materia == other.id_materia
