class Libro:
    def __init__(self, isbn: str, titulo: str, autor: str, numero_ejemplares: int, id_materia: int, id_curso: str):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.numero_ejemplares = numero_ejemplares
        self.id_materia = id_materia
        self.id_curso = id_curso

    def __str__(self):
        return f"{self.titulo} ({self.isbn}) - {self.autor} [{self.numero_ejemplares} ejemplares]"

    def __eq__(self, other):
        return isinstance(other, Libro) and self.isbn == other.isbn
