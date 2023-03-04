'''Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.'''

print ('Introduce un número: ')
numero = int(input())
while numero % 2 == 0:
    print ('Es par¡¡')
    break
else:
    print ('Es impar¡¡')