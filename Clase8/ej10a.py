'''
Ejercicio 10
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es 
un número primo o no.
'''

num = int(raw_input("Introduce un numero positivo mayor que 2: "))

i = 2
while num % i != 0:
    i += 1

if i == num:
    print("Es primo.")
else:
    print("No es primo.")