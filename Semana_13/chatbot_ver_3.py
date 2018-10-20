# importamos json para codificar nuestro diccionario y salvarlo
import json

def leer(archivo):
    """
    (str) -> dict
    Lee un archivo con un diccioniario en formato json
    :param archivo:
    :return:
    """
    try:
        archivo = open(archivo, 'r')
        conocimiento = json.load(archivo)
        archivo.close()
        return conocimiento
    except FileNotFoundError:
        return {}


def guardar(archivo, diccionario):
    """
    (str, dict) -> bool

    Guarda la información de un diccionario
    :param archivo:
    :param diccionario:
    :return:
    """
    try:
        archivo = open(archivo, 'w')
        archivo.write(json.dumps(diccionario))
        archivo.close()
        return True
    except:
        return False


def main():

    # Saludar
    print('Hola papi, soy esperanza, ')

    # Hacer un diccionario de conocimientos de Esperanza
    # A partir de un archivo
    conocimiento = leer('conocimiento.txt')



    despedidas = leer('despedidas.txt')

    # Mientras no se despida
    while True:

        # El usuario ingresa una peticion
        peticion = input('haz tu petición o despidete para salir ').lower().strip()

        # Si se despide salimos
        if peticion in despedidas:
            print(despedidas[peticion].capitalize())

            # Escribimos lo que aprendimos en la base de conocimiento
            guardar('conocimiento.txt', conocimiento)
            guardar('despedidas.txt', despedidas)
            # archivo = open('conocimiento.txt', 'w')
            # archivo.write(json.dumps(conocimiento))
            break

        # Si se la respuesta respondo
        elif peticion in conocimiento:
            print(conocimiento[peticion].capitalize())

        # Si no la se aprendo
        else:
            respuesta = input('¿Eso es una despedida? S/N ').lower().strip()
            if respuesta == 's':
                respuesta = input('¿Como debería despedirme? ').lower().strip()
                despedidas[peticion] = respuesta
                guardar('conocimiento.txt', conocimiento)
                guardar('despedidas.txt', despedidas)
                print('aprendi a despedirme ', respuesta)
                break
            else:
                respuesta = input('No se, ¿como debería responder a eso? ').lower().strip()
                conocimiento[peticion] = respuesta


main()
