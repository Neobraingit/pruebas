s = input('Introduce un string; ')
recorrido = 0
vocales = 0
while recorrido < len(s):
     if s[recorrido] == 'a' or s[recorrido] == 'e' or s[recorrido] == 'i' or s[recorrido] == 'o' or s[recorrido] == 'u':
          vocales += 1
     recorrido += 1
     
       
   
print (vocales)