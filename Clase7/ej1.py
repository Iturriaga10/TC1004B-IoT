"""Ejercicio 1
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces."""

word = input("Escribe una palabra: ")
word1 = input("Escribe una segunda palabra: ")

for variable in range(1, 11):
    print(str(variable) + ") " + word)

for variable in range(1, 6):
    print(str(variable) + ") " + word1)
