from random import randint

matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(matriz)

def matriz_cuadrada(n):
    """
    Genera una matriz aleatoria con de tamaño n x n
    :param n:
    :return:
    """
    matriz = []
    for i in range(0, n):
        fila = []
        for j in range(0,n):
            fila.append(randint(0,9))
        matriz.append(fila)
    return matriz

print(matriz_cuadrada(4))

def gen_matriz(filas, columnas):
    matriz = []
    for i in range(0, filas):
        fila = []
        for j in range(0,columnas):
            fila.append(randint(0,9))
        matriz.append(fila)
    return matriz

print(gen_matriz(3, 5))

def intercambio_filas(matriz, f1, f2):
    """
    Intercambia dos filas en una matriz

    >>> intercambio_filas([[1],[2]], 0, 1)
    [[2],[1]]

    :param matriz:
    :param f1:
    :param f2:
    :return:
    """
    resultante = matriz.copy()
    fila_temporal = resultante[f1]
    resultante[f1] = resultante[f2]
    resultante[f2] = fila_temporal
    return resultante

print(intercambio_filas([[1,2],[2,1]], 0, 1))

def producto_escalar(vector, escalar):
    resultante = []
    for elem in vector:
        resultante.append(elem * escalar)
    return resultante

def producto_fila(matriz, fila, escalar):
    resultante = matriz.copy()
    resultante[fila] = producto_escalar(resultante[fila], escalar)
    return resultante

def suma_vectores(v1, v2):
    resultante = []
    for i in range(0, len(v1)):
        resultante.append(v1[i] + v2[i])
    return resultante

def suma_filas(matriz, fila_origen, fila_destino, veces):
    resultante = matriz.copy()
    fila_a_sumar = producto_escalar(resultante[fila_origen], veces)
    resultante[fila_origen] = suma_vectores(fila_a_sumar, resultante[fila_destino])
    return resultante

