'''
Ejercicio 13
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que 
el usuario escriba “salir” que terminará.
'''

while True:
    frase = raw_input("Introduce algo: ")
    if frase.lower() == "salir":
        break
    print(frase)