'''
Ejercicio 10
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es 
un número primo o no.
'''

num = int(raw_input("Introduce un numero positivo mayor que 2: "))

for i in range(2, num):
    if num % i == 0:
        break

if (i+1) == num:
    print("Es primo.")
else:
    print("No es primo.")