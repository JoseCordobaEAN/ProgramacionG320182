def union_diccionarios(dic1, dic2):
    """
    (dict, dict) -> dict

    Hace la union entre los dos diccionarios

    >>> union_diccionarios({'hola':'mundo'}, {'mundo': 'hola'} )
    {'hola': 'mundo', 'mundo': 'hola'}
    >>> union_diccionarios({'hola':'mundo', 'mundo': 'hola'}, {'jose':'cordoba'} )
    {'hola': 'mundo', 'mundo': 'hola', 'jose': 'cordoba'}
    >>> union_diccionarios({}, {'hola':'mundo', 'mundo': 'hola', 'jose':'cordoba'})
    {'hola': 'mundo', 'mundo': 'hola', 'jose': 'cordoba'}
    >>> union_diccionarios({'hola':'mundo', 'mundo': 'hola', 'jose':'cordoba'}, {})
    {'hola': 'mundo', 'mundo': 'hola', 'jose': 'cordoba'}

    :param dic1:
    :param dic2:
    :return:
    """
    dict_resultante = dic1.copy()
    for llave in dic2:
        dict_resultante[llave] = dic2[llave]
    return dict_resultante


def maximo_diccionario(dic):
    """
    (dict) -> obj

    retorna el elemento maximo en un diccionario el diccionario no puede ser vacio

    >>> maximo_diccionario({'hola': 10, 'mundo': 5, 'pepe': 30, 'cam': 9})
    30
    >>> maximo_diccionario({'hola': "a", 'mundo': "b", 'pepe': "ñ", 'cam': "t"})
    'ñ'

    :param dic:
    :return:
    """
    if dic:
        bandera = True
        mayor = None
        for llave in dic:
            if not bandera and mayor < dic[llave]:
                mayor = dic[llave]
            elif bandera:
                mayor = dic[llave]
                bandera = False
        return mayor
