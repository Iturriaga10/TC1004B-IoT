"""Ejercicio 1
Escribe un algoritmo para verificar si un precio dado por el usuario es válido o no lo es, para 
ser válido debe ser un valor positivo."""

precio = float(input("Escriba un precio en pesos: "))
if precio < 0:
    print("Valor no valido ")
