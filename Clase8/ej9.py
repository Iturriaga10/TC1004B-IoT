'''
Ejercicio 9
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
'''

pwd = "ClaseG102.1"

pwd_usr = ""
while pwd != pwd_usr: # == igual, != desigual
    pwd_usr = raw_input("Introduzca su contrasena: ")

print("Contrasena Correcta")