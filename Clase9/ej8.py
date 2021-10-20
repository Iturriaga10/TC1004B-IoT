'''
Ejercicio 8
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un 
palíndromo.
'''

palabra = list(raw_input("introduce una palabra: "))

if palabra[::-1] == palabra:
    print("Palindromo")
else:
    print("No es Palindromo")
