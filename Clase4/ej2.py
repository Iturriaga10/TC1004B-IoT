"""Ejercicio 2
Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo 
¡hola <nombre>!."""


def nombre(valueInput):
    print("Hola " + valueInput)


name = input("Escriba su nombre: ")
nombre(name)
