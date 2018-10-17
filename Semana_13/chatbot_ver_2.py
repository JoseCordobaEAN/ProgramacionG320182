# importamos json para codificar nuestro diccionario y salvarlo
import json

# Saludar
print('Hola papi, soy esperanza, ')

# Hacer un diccionario de conocimientos de Esperanza
# A partir de un archivo
try:
    archivo = open('conocimiento.txt', 'r')
    conocimiento = json.load(archivo)
    archivo.close()
except FileNotFoundError:
    conocimiento = {'hola': 'hola, ¿como estas?',
                'que haces': 'chateando contigo',
                'cuantos años tienes': 'tengo 10 segundos de ejecución',
                'quien es usted': 'soy estudiante',
                'no lo escuché': 'soy estudiante',
                'una vez mas': 'soy estudiante, soy soy, estudiante soy, yo quiero estudiar, para cambiar la sociedad'}

    print('No se nada')



despedidas = ['chao', 'suerte', 'hasta luego', 'hasta mañana', 'vemos', 'nos vidrios', 'adios']




# Mientras no se despida
while True:

    # El usuario ingresa una peticion
    peticion = input('haz tu petición o despidete para salir ').lower().strip()

    # Si se despide salimos
    if peticion in despedidas:
        print('Nos pi')

        # Escribimos lo que aprendimos en la base de conocimiento
        archivo = open('conocimiento.txt', 'w')
        archivo.write(json.dumps(conocimiento))
        break

    # Si se la respuesta respondo
    elif peticion in conocimiento:
        print(conocimiento[peticion].capitalize())

    # Si no la se aprendo
    else:
        respuesta = input('No se, ¿como debería responder a eso? ')
        conocimiento[peticion] = respuesta
