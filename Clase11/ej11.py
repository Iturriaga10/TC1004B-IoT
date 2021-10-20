'''
Ejercicio 11
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre 
por pantalla su producto escalar.
'''

vector1 = (1,2,3)
vector2 = (-1,0,2)

total = 0
for x in range(0, len(vector1)):
    total += vector1[x] * vector2[x] # total = total + vector1[x] * vector2[x])

print("Producto escalar = " + str(total) )