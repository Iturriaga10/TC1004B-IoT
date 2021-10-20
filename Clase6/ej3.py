"""Ejercicio 3
Escribir una función que calcule el módulo de un vector."""

import math


def vector(x, y):
    return math.sqrt(x ** 2 + y ** 2)


x = float(input("Escribe el valor de x: "))
y = float(input("Escribe el valor de y: "))

print("El modulo es: " + str(vector(x, y)))
