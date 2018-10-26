class Ingrediente:
    """
    Representa un ingrediente para mi postribulo
    """

    nombre = ""
    sabor = ""
    cantidad = 0.0
    procesado = False

    def __init__(self, nombre, sabor, cantidad):
        """
        Crea un nuevo ingrediente
        :param nombre: {str} el nombre del ingrediente
        :param sabor: el sabor del ingrediente
        :param cantidad: La cantidad del ingrediente
        """
        self.nombre = nombre
        self.cantidad = cantidad
        self.sabor = sabor

    def __repr__(self):
        """
        Crea una cadena que representa el ingrediente
        :return:
        """
        return self.nombre + ' ' + self.sabor + " por " + str(self.cantidad)

    def __eq__(self, other):
        if type(self) == type(other):
            return self.nombre == other.nombre \
                   and self.sabor == other.sabor \
                   and self.cantidad == other.cantidad
        else:
            raise ValueError("No se puede comparar ingredientes con "
                             +type(other))

    def picar(self):
        """
        Procesa el ingrediente para picarlo

        :return: la nueva cantidad disponible del ingrediente
        """
        self.procesado = True
        self.cantidad *= 80 / 100
        return self.cantidad





