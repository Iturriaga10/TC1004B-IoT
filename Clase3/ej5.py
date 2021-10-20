"""Ejercicio 5
Escribe un algoritmo que dada una longitud en metros, calcule y muestre su equivalente en pies.
Recuerda que 1 pie = 12 pulgadas, 1 pulgada = 2.54 cm, 1 m = 100 cm . Una vez realizado el 
algoritmo crear un programa en Python que solucione este problema.
1. Ingresar longitud en metros.
2. Convertir de metros a centimetros.
3. Convertir de centimetros a pulgadas.
4. Convertir pulgadas a pies.
5. Imprimir el resultado"""


longitud = input("Ingrese la longitud en metros: ")

conv_foot = ((float(longitud) * 100) / 2.5) / 12
# conv_cm = float(longitud) * 100
# conv_inch = conv_cm / 2.5
# conv_foot = conv_inch / 12
print("El resultado en pies es: " + str(conv_foot))
