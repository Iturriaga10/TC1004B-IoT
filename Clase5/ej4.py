"""Ejercicio 4
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al 
usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario 
coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas."""

pwd = "clase102"
pwd_ingresada = input("Escriba su contrasena: ")
# No olvien que debe de llevar doble igual la condicional :)
if pwd == pwd_ingresada:
    print("Coinciden")
else:
    print("Contrasena incorrecta")
