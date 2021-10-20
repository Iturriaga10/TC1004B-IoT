"""Ejercicio 4
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número 
introducido."""


def times(nombre, count):
    print((" %s" % nombre) * count)


nombre = input("Escriba su nombre: ")
count = int(input("Escriba el numero de veces: "))
times(nombre, count)
