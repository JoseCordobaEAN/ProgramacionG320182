# Hacer un diccionario de conocimientos de Esperanza
conocimiento = {'hola': 'hola, ¿como estas?',
                'que haces': 'chateando contigo',
                'cuantos años tienes': 'tengo 10 segundos de ejecución',
                'quien es usted': 'soy estudiante',
                'no lo escuché': 'soy estudiante',
                'una vez mas': 'soy estudiante, soy soy, estudiante soy, yo quiero estudiar, para cambiar la sociedad'}

# Saludar
print('Hola papi, soy esperanza, ')

# El usuario ingresa una peticion
peticion = input('haz tu petición ')

# Si se la respuesta respondo
if peticion in conocimiento:
    print(conocimiento[peticion])

# Si no la se aprendo
else:
    respuesta = input('No se, ¿como debería responder a eso? ')
    conocimiento[peticion] = respuesta
