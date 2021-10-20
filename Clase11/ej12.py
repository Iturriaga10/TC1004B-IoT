'''
Ejercicio 12
Escribir un programa que almacene las matrices en una lista y muestre por pantalla su 
producto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando 
cada vector fila en una lista.
'''

a = ((1, 2, 3),
     (4, 5, 6))

b = ((-1, 0),
     (0, 1),
     (1,1))

result = [[0,0],
          [0,0]]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]

# Covertir en Tupla
for i in range(len(result)):
    result[i] = tuple(result[i])

result = tuple(result)

# Imprimir resultado
for i in range(len(result)):
    print(result[i])