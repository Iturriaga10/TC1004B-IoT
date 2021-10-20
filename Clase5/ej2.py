"""Ejercicio 2
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad 
o no."""

edad = float(input("Escriba su edad: "))
if edad < 18:
    print("Usted es menor de edad. ")
# Opcion 2
# if edad >= 18:
#    print("Usted es mayor de edad.")
# Opcion 1
else:
    print("Usted es mayor de edad.")
