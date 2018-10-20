# Hacer un diccionario de conocimientos de Esperanza
conocimiento = {'hola': 'hola, ¿como estas?',
                'que haces': 'chateando contigo',
                'cuantos años tienes': 'tengo 10 segundos de ejecución',
                'quien es usted': 'soy estudiante',
                'no lo escuché': 'soy estudiante',
                'una vez mas': 'soy estudiante, soy soy, estudiante soy, yo quiero estudiar, para cambiar la sociedad'}

despedidas = ['chao', 'suerte', 'hasta luego', 'hasta mañana', 'vemos', 'nos vidrios', 'adios']

# Saludar
print('Hola papi, soy esperanza, ')


# Mientras no se despida
while True:

    # El usuario ingresa una peticion
    peticion = input('haz tu petición o despidete para salir ').lower().strip()

    # Si se despide salimos
    if peticion in despedidas:
        print('Nos pi')
        break

    # Si se la respuesta respondo
    elif peticion in conocimiento:
        print(conocimiento[peticion].capitalize())

    # Si no la se aprendo
    else:
        respuesta = input('No se, ¿como debería responder a eso? ')
        conocimiento[peticion] = respuesta
