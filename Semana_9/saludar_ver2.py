# Saludar hasta que diga chao
mensaje = 'dime algo y lo repetiré hasta que me digas "chao"'
ingresado = ""
bandera = True
while bandera:
    ingresado = input(mensaje)
    bandera = ingresado.lower() != 'chao'
    if bandera:
        print(ingresado)
