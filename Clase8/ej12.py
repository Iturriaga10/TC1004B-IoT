'''
Ejercicio 12
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y 
muestre por pantalla el número de veces que aparece la letra en la frase.
'''

frase = raw_input("Introduce una frase: ").lower()
letra = raw_input("Introduce una letra: ").lower()

contador = 0

for x in frase:
    if x == letra:
        contador += 1 # contador = contador + 1

if contador == 0:
    print("Error: \n \t La frase contiene 0 apariciones")
    # \n --> Salto de linea.
    # \t --> Tab.    
else:
    print("La letra \"%s\" aparece %i veces en la frase" %(letra, contador))
    # print("La letra '%s' aparece %i veces en la frase" %(letra, contador))

    # %s --> string
    # %i --> int
