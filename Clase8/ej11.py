'''
Ejercicio 11
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una 
a una las letras de la pala‐ bra introducida empezando por la última.
'''

word = raw_input("Introduzca una palabra: ")

# [ 0, 1, 2, 3]
# ["Hola"]

for i in range(len(word)-1, -1, -1):
    print(word[i])