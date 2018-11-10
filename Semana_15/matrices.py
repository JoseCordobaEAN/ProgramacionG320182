from random import randint

matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print("Imprimiendo una matriz ", matriz)

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

print("Imprimiendo una matriz cuadrada", matriz_cuadrada(4))

def gen_matriz(filas, columnas):
    matriz = []
    for i in range(0, filas):
        fila = []
        for j in range(0,columnas):
            fila.append(randint(0,9))
        matriz.append(fila)
    return matriz

print("Imprimiendo una matriz 3 x 5", gen_matriz(3, 5))

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

print("Imprimiendo ejemplo de intercambio de filas ",intercambio_filas([[1,2],[2,1]], 0, 1))

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
    resultante[fila_destino] = suma_vectores(fila_a_sumar, resultante[fila_destino])
    return resultante

def reducir_matriz(matriz):
    resultante = matriz.copy()
    for i in range(0, len(resultante)):
        resultante[i] = producto_escalar(resultante[i], 1 / resultante[i][i])
        for j in range(i + 1, len(resultante)):
            resultante = suma_filas(resultante, i, j, -resultante[j][i])
    return resultante

print("Imprimiendo Reduccion de una matriz", reducir_matriz([[1, 2],[2, 1]]))
print("Imprimiendo Reduccion de una matriz", reducir_matriz([[1, 2, 3],[3, 2, 1], [1, 2, 5]]))

def suma_matriz(A, B):
    resultante = []
    # Recorremos las filas de la matriz
    for i in range(0, len(A)):
        fila = []

        # Recorremos las columnas
        for j in range (0, len(A[i])):

            # Sumamos los escalares
            fila.append(A[i][j] + B[i][j])
        # Insertamos la fila a la matriz
        resultante.append(fila)
    return resultante


print("Imprimiendo matriz a sumar", matriz)
print("Imprimiendo Suma por si misma", suma_matriz(matriz, matriz))


