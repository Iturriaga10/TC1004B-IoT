'''
Ejercicio 3
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio 
de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un 
mensaje informando de ello.
'''
fruta_user = input("Escribe la fruta: ").lower().replace("á", "a")
print(fruta_user)
peso = int(input("Escribe el peso: "))

frutas = { "platano": 1.35, "manzana": .80, "pera":.85, "naranja":.70 }

if fruta_user in frutas:   
        total = peso * frutas[fruta_user]
        print("El costo de %s es de %s" %(fruta_user, str(total)))
else:
        print("La fruta no existe.")
