"""Ejercicio 9
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre
<m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el
usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente."""

n = float(input("Escriba el 1er numero: "))
m = float(input("Escriba el 2do numero: "))
result = n / m
rest = n % m

print("El resultado es " + str(int(result)) + " y el cociente es " + str(rest))
