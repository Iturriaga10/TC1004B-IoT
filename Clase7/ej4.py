"""Ejercicio 4
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la 
cuenta atrás desde ese número hasta cero separados por comas."""

numero = int(input("Escriba un numero entero positivo: "))

out = ""
for y in range(numero, -1, -1):
    out += str(y) + ", "  # out = out + str(y) + ", "

print(out)
