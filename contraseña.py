'''Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña e imprima por 
pantalla si la contraseña introducida por el usuario coincide con 
la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.'''

password = input('Introduce tu password: ')
usuario = input('Introduce una contraseña: ').lower()
if usuario == password:
    print ('Puedes entrar¡¡')
while usuario != password:
    usuario = input('Introduce una contraseña: ')
else:
    print ('Puedes entrar¡¡')
    



  