# Saludar hasta que diga chao
mensaje = 'dime algo y lo repetiré hasta que me digas "chao"'
ingresado = ""
while ingresado.lower() != 'chao':
    ingresado = input(mensaje)
    print(ingresado)
