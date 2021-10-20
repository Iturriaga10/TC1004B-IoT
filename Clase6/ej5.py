"""Ejercicio 5
Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre 
por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra
con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos 
en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como 
quiera."""


def mayuscula(nombre):
    return nombre.upper()


def minuscula(nombre):
    return nombre.lower()


def capital(nombre):
    return nombre.capitalize()


nombre = input("Escribe tu nombre: ")
print(mayuscula(nombre))
print(minuscula(nombre))
print(capital(nombre))
