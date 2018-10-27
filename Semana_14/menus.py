# Vamos a hacer una serie de funciones que luego el usuario va a poder consultar a traves de un menu

def valor_absoluto(num):
    if num < 0:
        return -num
    return num


def suma(lista):
    resultado = 0
    for elemento in lista:
        resultado += elemento
    return resultado

def resta(lista):
    resultado = 0
    for elemento in lista:
        resultado -= elemento
    return resultado

def leer_lista():
    lista = []
    while True:
        elemento = input('ingrese un numero a la lista o q para terminar ')
        if elemento.lower() != 'q':
            lista.append(float(elemento))
        else:
            break
    return lista


def main():
    lista = []
    while True:
        opcion = input('Bienvenido al programa, seleccione que desea hacer:\n'
              '1. valor absoluto\n'
              '2. Ingresar una lista\n'
              '3. Sumar los elementos de la lista\n'
              '4. Restar los elementos de la lista\n'
              '5. Salir\n')

        if opcion == '1':
            numero = int(input('Ingrese su numero '))
            print('el valor absoluto de su numero es '+ str(valor_absoluto(numero)))
        elif opcion == '2':
            lista = leer_lista()
            print('Su lista es '+str(lista))
        elif opcion == '3':
            resultado = suma(lista)
            print('la suma de los elementos en '+str(lista)+ " es "+ str(resultado))
        elif opcion == '4':
            resultado = resta(lista)
            print('la resta de los elementos en '+str(lista)+ " es "+ str(resultado))
        elif opcion == '5':
            print("Gracias por usar el programa")
            break
        else:
            print('opcion no valida')

main()
