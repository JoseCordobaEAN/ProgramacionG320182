# Saludar hasta que diga chao rompiendo el while
mensaje = 'dime algo y lo repetiré hasta que me digas "chao"'

while True:
    ingresado = input(mensaje)
    if ingresado.lower() == 'chao':
        break;
    print(ingresado)

