'''
Escribir un programa que pregunte el nombre el un producto, su precio y un número 
de unidades y muestre por pantalla una cadena con el nombre del producto
seguido de su precio unitario con 6 dígitos enteros y 2 decimales,
el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.'''

print ('Dime el nombre del producto: ')
nombre = input()
print ('Dime su precio: ')
precio = input()
print ('Dime cuántas unidades quieres: ')
unidades = input()

print ('El nombre del producto es {}, su precio es {} y sus unidades son {}'.format(nombre, precio, unidades))