# Un diccionario es una estructura lineal de datos donde los elementos
# Estan almacenados en parejas llave valor
# Por ejemplo
seriales_partes = {'motor': 123456, 'chasis': 7897546}
print(seriales_partes)

# Puedo acceder a un solo elemento por su llave
print(seriales_partes['motor'])

# Puedo agregar nuevos elementos a mi diccionario
seriales_partes['radio'] = 456789
print(seriales_partes)

# Puedo consultar si tengo una llave en mi diccionario
print('caja de cambios' in seriales_partes)
print('chasis' in seriales_partes)

# Puedo editar valores en mi diccionario
seriales_partes['motor'] = 789645231
print(seriales_partes['motor'])

# Esto no hacerlo, esta muy chambon
# seriales_partes["motor"] = [seriales_partes['motor'], 12356]
# print(seriales_partes)

# Podemos recorrer un diccionario usando for
for llave in seriales_partes:
    print(llave, seriales_partes[llave])

# print(type(seriales_partes))

# Puedo usar pop para sacar un elemento del diccionario
motor = seriales_partes.pop('motor')
print(motor)
print(seriales_partes)



