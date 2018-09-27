# Imprimir los numeros impares del 1 al 10
num = 0
print('\nImprimiendo los numeros impares entre 1 y 10')
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)

num = 1

# Otra versión
print('\nImprimiendo los numeros impares entre 1 y 10')
while num < 10:
    print(num)
    num +=2

# Version con For
print('\nImprimiendo los numeros impares entre 1 y 10')
for i in range (1, 10, 2):
    print(i)
