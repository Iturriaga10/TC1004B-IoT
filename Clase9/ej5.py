'''
Ejercicio 5
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre 
por pantalla en orden inverso separados por comas.
'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Solucion 1
reversa=""
for i in range(1, 11):
    reversa+=str(numeros[-i])+ ", "

print(reversa)

# Solucion 2
numeros.reverse()

reversa=""
for numero in numeros:
    reversa+=str(numero)+ ", "

print(reversa)
