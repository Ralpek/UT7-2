class Prestamo:
    def __init__(self, nie, isbn, fecha_entrega, fecha_devolucion='', estado='P'):
        self.nie = nie
        self.isbn = isbn
        self.fecha_entrega = fecha_entrega
        self.fecha_devolucion = fecha_devolucion
        self.estado = estado

    def __str__(self):
        return (f"NIE: {self.nie}, ISBN: {self.isbn}, Entrega: {self.fecha_entrega}, "
                f"Devolución: {self.fecha_devolucion}, Estado: {self.estado}")

    def __eq__(self, other):
        return isinstance(other, Prestamo) and self.nie == other.nie and self.isbn == other.isbn

    def actualizar(self, fecha_devolucion, estado):
        self.fecha_devolucion = fecha_devolucion
        self.estado = estado
