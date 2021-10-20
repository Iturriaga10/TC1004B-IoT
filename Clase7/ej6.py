"""Ejercicio 6
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
rectángulo como el de más abajo, de altura el número introducido."""


altura = int(input("Introduce la altura del triangulo: "))

# for h in range(1, altura + 1):
#    print("*" * h)

out = ""
for j in range(1, altura+1):
    out += "*"
    print(out)
