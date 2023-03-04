'''Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.'''

num1 = int(input('Introduce un número: '))
num2  = int(input('Introduce otreo número: '))
if num1 / num2 == 0:
    print ('Error, este número es cero')
else:
    print ('Perfecto¡¡ El número es válido¡¡')