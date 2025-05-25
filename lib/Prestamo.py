class Prestamo:
    def __init__(self, nie: str, id_curso: str, isbn: str, fecha_entrega, fecha_devolucion, estado: bool):
        self.nie = nie
        self.id_curso = id_curso
        self.isbn = isbn
        self.fecha_entrega = fecha_entrega
        self.fecha_devolucion = fecha_devolucion
        self.estado = estado

    def __str__(self):
        estado_str = 'Devuelto' if self.estado else 'Prestado'
        return f"NIE: {self.nie}, ISBN: {self.isbn}, Entrega: {self.fecha_entrega}, Devolución: {self.fecha_devolucion}, Estado: {estado_str}"

    def __eq__(self, other):
        return (
            isinstance(other, Prestamo) and
            self.nie == other.nie and
            self.id_curso == other.id_curso and
            self.isbn == other.isbn
        )
