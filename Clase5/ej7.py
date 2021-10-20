"""Ejercicio 7
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El 
grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre 
posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su 
nombre y sexo, y muestre por pantalla el grupo que le corresponde."""

name = input("Escriba su nombre: ")
sex = input("Escriba su sexo: ")

first_letter = name[0].lower()  # Patricio

# AND / OR / NOT

if first_letter < "m" and sex == "mujer":
    print(" Pertences al grupo A")
elif first_letter > "m" and sex == "mujer":
    print(" Pertences al grupo B")
elif first_letter < "n" and sex == "hombre":
    print(" Pertences al grupo A")
elif first_letter > "n" and sex == "hombre":
    print(" Pertences al grupo B")
else:
    print("Escribe bien, hombre o mujer en el sexo.")
