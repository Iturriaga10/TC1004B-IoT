"""Ejercicio 3
Escribir una función que reciba un número entero positivo y devuelva su factorial."""

import math


def factortial(x):
    return math.factorial(x)


value = int(input("Ingrese un numero: "))
print(factortial(value))
