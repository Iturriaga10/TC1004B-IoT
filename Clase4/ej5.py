"""Ejercicio 5
Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un 
cilindro usando la primera función."""

import math


def circulo(radio):
    return math.pi * radio ** 2


def cilindro(radio, altura):
    return circulo(radio) * altura


print(cilindro(3, 5))
