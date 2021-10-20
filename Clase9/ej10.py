'''
Ejercicio 10
Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
'''
numeros = [50, 75, 46, 22, 80, 65, 8]

numeros.sort()

print("El minimo es: " + str(numeros[0]) + " el maximo es: " + str(numeros[len(numeros)-1] ))

