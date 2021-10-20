"""Ejercicio 1
Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, 
tangente, exponencial y logaritmo neperiano. La función preguntará al usuario el valor y la 
función a aplicar, y mostrará por pantalla una tabla con los enteros de 1 al valor introducido 
y el resultado de aplicar la función a esos enteros."""

import math


def calculadora(value, numero):
    if value == 0:
        return math.sin(numero)
    elif value == 1:
        return math.cos(numero)
    elif value == 2:
        return math.tan(numero)
    elif value == 3:
        return math.exp(numero)
    elif value == 4:
        return math.log(numero)
    else:
        return "Error"


numero = float(input("Ingrese el valor que desea calcular: "))
print("0) Seno, 1) Coseno, 2) Tangente, 3) Exponencial y 4)Logaritmo")
value = int(input("Ingresa la operacion a realizar  : "))
print("El resultado de la operacion es: " + str(calculadora(value, numero)))
