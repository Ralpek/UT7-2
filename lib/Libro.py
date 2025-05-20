class Libro:
    def __init__(self, isbn, titulo, autor, numero_ejemplares):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.numero_ejemplares = numero_ejemplares

    def __str__(self):
        return f"ISBN: {self.isbn}, Título: {self.titulo}, Autor: {self.autor}, Ejemplares: {self.numero_ejemplares}"

    def __eq__(self, other):
        return isinstance(other, Libro) and self.isbn == other.isbn

    def actualizar(self, titulo, autor, numero_ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.numero_ejemplares = numero_ejemplares
