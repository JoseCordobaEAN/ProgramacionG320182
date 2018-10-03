def de_la_z_a_la_a():
    """
    () -> list of str

    >>> de_la_z_a_la_a()
    ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

    :return: list con las letras de la z a la a
    """
    resultado = []
    contador = 122
    while contador > 96:
        resultado.append(chr(contador))
        contador -= 1
    return resultado


def suma_pares(inferior, superior):
    """
    (int, int) -> int

    Calcula la suma de todos los numeros pares en el rango inclusive

    >>> suma_pares(0, 10)
    30
    >>> suma_pares(2, 5)
    6
    >>> suma_pares(0, -1)
    0

    :param inferior: El limite inferior del rango
    :param superior: El limite superior del rango
    :return: La suma de todos los números pares en el rango
    """
    pass


def digitos(numero):
    """
    (int) -> int

    Cuenta el numero de digitos dado un entero

    >>> digitos(10)
    2
    >>> digitos(1967)
    4
    >>> digitos(-20)
    2
    >>> digitos(0)
    1

    :param numero:
    :return:
    """
    contador = 1
    copia = abs(numero)
    while copia >= 10:
        contador += 1
        copia //= 10
    return contador

def suma_digitos(numero):
    """
    (int) -> int

    Cuenta el numero de digitos dado un entero

    >>> suma_digitos(10)
    1
    >>> suma_digitos(1967)
    23
    >>> suma_digitos(-20)
    2
    >>> suma_digitos(0)
    0

    :param numero:
    :return:
    """
    acumulador = 0
    copia = abs(numero)
    while copia > 0:
        acumulador += copia % 10
        copia //= 10
    return acumulador


def lista_digitos(numero):
    """
    (int) -> int

    Cuenta el numero de digitos dado un entero

    >>> lista_digitos(10)
    [1, 0]
    >>> lista_digitos(1967)
    [1, 9, 6, 7]
    >>> lista_digitos(-20)
    [-2, 0]
    >>> lista_digitos(0)
    [0]

    :param numero:
    :return:
    """
    if numero == 0:
        return [0]
    acumulador = []
    bandera_neg = numero < 0
    copia = abs(numero)
    while copia > 0:
        acumulador.insert(0, copia % 10)
        copia //= 10
    if bandera_neg:
        acumulador[0] *= -1
    return acumulador
