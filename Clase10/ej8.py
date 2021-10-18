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




