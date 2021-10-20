"""Ejercicio 3
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos 
los números impares desde 1 hasta ese número separados por comas."""

numero = int(input("Escriba un numero entero positivo: "))

out = ""
for y in range(1, numero + 1, 2):
    out += str(y) + ", "  # out = out + str(y) + ", "

print(out)
