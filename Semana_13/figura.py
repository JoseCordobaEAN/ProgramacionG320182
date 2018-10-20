class Figura:
    """
    La clase figura representa una figura geometrica
    """

    cantidad_lados = 0
    longitud_lados = []

    def __init__(self, c_lados, longitud_lados):
        """
        (int, list of float) -> Figura

        Crea una nueva figura

        :param c_lados: cuantos lados tiene la figura
        :param longitud_lados: Lista con la longitud de los lados
        :return: Una nueva instancia de la figura
        """
        self.cantidad_lados = c_lados
        self.longitud_lados = longitud_lados.copy()

    def perimetro(self):
        """
        Calcula el perimetro de la figura

        :return: el perimetro de la figura
        """
        return sum(self.longitud_lados)
        # perimetro = 0
        # for lado in self.longitud_lados:
        #     perimetro += lado
        # return perimetro


    def __repr__(self):
        """
        Retorna una representación de la figura
        :return:
        """
        return 'Esta es una figura de '+ str(self.cantidad_lados) \
               +' lados  que miden ' + str(self.longitud_lados)
