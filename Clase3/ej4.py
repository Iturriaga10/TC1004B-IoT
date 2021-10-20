"""Ejercicio 4
Escribe un algoritmo que muestre la velocidad promedio de un automóvil dadas la distancia recorrida 
en kilómetros y el tiempo que se tardó en recorrer esa distancia dado en horas. Una vez realizado 
el algoritmo crear un programa en Python que solucione este problema.

1. Obtener la distancia que recorrió el vehículo en kilómetros.
2. Obtener el tiempo que recorrió el vehículo en horas.
3. Realizar el cálculo, utilizando los datos previamente obtenidos.
4. Mostrar el resultado obtenido

                V= d/t"""

distance = input("Escriba su distancia en kilometros: ")
time = input("Escriba su tiempo en horas: ")
vel = float(distance) / float(time)
print("La velocidad es " + str(vel) + " " + "km/hr")
