"""Ejercicio 2
Escribir una función que reciba una frase y devuelva su longitud."""


def longitud(frase):
    return len(frase)


frase = input("Ingrese la frase deseada: ")
print("La longitud de la frase es: " + str(longitud(frase)))
