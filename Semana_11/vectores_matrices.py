def suma_escalar(escalar, vector):
    """
    (num, list of num) -> list of num

    Suma el escalar a cada uno de los componentes del vector

    >>> suma_escalar(10, [3, 2, 7, 20])
    [13, 12, 17, 30]
    >>> suma_escalar(0, [3, 2, 7, 20])
    [3, 2, 7, 20]
    >>> suma_escalar(9, [3, 2, 7, 20])
    [12, 11, 16, 29]

    :param escalar:
    :param vector:
    :return:
    """
    acumulador = []
    for componente in vector:
        acumulador.append(componente + escalar)
    return acumulador


def producto_escalar(escalar, vector):
    """
    (num, list of num) -> list of num

    Multiplica el escalar a cada uno de los componentes del vector

    >>> producto_escalar(0, [3, 2, 7, 20])
    [0, 0, 0, 0]
    >>> producto_escalar(2, [3, 2, 7, 20])
    [6, 4, 14, 40]
    >>> producto_escalar(7, [3, 2, 7, 20])
    [21, 14, 49, 140]

    :param escalar:
    :param vector:
    :return:
    """
    clon = vector[:]
    acumulador = []
    while clon:
        acumulador.insert(0, clon.pop() * escalar)
    #print(vector)
    return acumulador


def suma_vectores(v1, v2):
    """
    (list of num, list of num) -> list of num

    Calcula la suma de dos vectores

    >>> suma_vectores([1, 2, 3], [1, 2, 3])
    [2, 4, 6]
    >>> suma_vectores([2, 2, 2], [1, 2, 3])
    [3, 4, 5]
    >>> suma_vectores([1, 2, 3, 4], [1, 2, 3])
    Traceback (most recent call last):
    ...
    ValueError: Los vectores tienen diferente dimensión

    :param v1:
    :param v2:
    :return:
    """
    if len(v1) == len(v2):
       resultante = []
       for i in range(0, len(v1)):
           resultante.append(v1[i] + v2[i])
       return resultante
    else:
       raise ValueError('Los vectores tienen diferente dimensión')


def producto_punto(v1, v2):
    """
    (list of num, list of num) -> num

    Calcula el producto punto de dos vectores

    >>> producto_punto([1, 2, 3], [1, 2, 3])
    14
    >>> producto_punto([2, 2, 2], [1, 2, 3])
    12
    >>> producto_punto([1, 2, 3, 4], [1, 2, 3])
    Traceback (most recent call last):
    ...
    ValueError: Los vectores tienen diferente dimensión

    :param v1:
    :param v2:
    :return:
    """
    if len(v1) == len(v2):
       resultado = 0
       for i in range(0, len(v1)):
           resultado += v1[i] * v2[i]
       return resultado
    else:
       raise ValueError('Los vectores tienen diferente dimensión')


def son_perpendiculares(v1, v2):
    """
    (list of num, list of num) -> bool

    Determina si dos vectores son perpendiculares

    >>> son_perpendiculares([1, 2], [-2, 1])
    True
    >>> son_perpendiculares([2, 4, 5], [-2, 3, 7])
    False
    >>> son_perpendiculares([2, -3, -1], [-5, -10/3, 0])
    True

    :param v1:
    :param v2:
    :return:
    """
    return producto_punto(v1, v2) == 0
