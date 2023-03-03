print ('Debes introducir un número  con este formato:  prefijo-número-extensión: ')
numero = input()
extension = numero[0:2]
print ('La extensión es: ',extension)
telefono = numero[3:12]
print ('El teléfono es: ',telefono)
prefijo = numero[13:15]
print ('El prefijo es:', prefijo)