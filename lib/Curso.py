class Curso:
    def __init__(self, id_curso: str, nivel: str):
        self.id_curso = id_curso
        self.nivel = nivel

    def __str__(self):
        return f"{self.id_curso} - Nivel: {self.nivel}"

    def __eq__(self, other):
        return isinstance(other, Curso) and self.id_curso == other.id_curso
