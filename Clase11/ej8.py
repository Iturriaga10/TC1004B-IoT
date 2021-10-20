'''
Ejercicio 8
Escribir un programa que cree un diccionario de traducción español-inglés. El usuario 
introducirá las palabras en español e inglés separadas por dos puntos, y cada par 
<palabra>:<traducción> separados por comas. El programa debe crear un diccionario con 
las palabras y sus traducciones. Después pedirá una frase en español y utilizará el 
diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario 
debe dejarla sin traducir.
'''

diccionario = { "palabra": "word", "hola":"hello", "adios": "bye" }

continuar = True
while continuar:
    palabra = raw_input("Introduce la palabra por agregar: ").lower().split(":")
    # Agrega nuevos elementos a un diccionario.
    diccionario.setdefault(palabra[0], palabra[1]) 
    continuar = raw_input("Desea Continuar: ").lower() == "si"

frase = raw_input("Escribe una frase: ").lower().split()

nueva_frase = ""
for palabra in frase:
    if palabra in diccionario:
        nueva_frase += diccionario[palabra] + " "
    else:
        nueva_frase += palabra + " "

print(nueva_frase.capitalize())




