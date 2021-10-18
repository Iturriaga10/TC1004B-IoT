fruta_user = input("Escribe la fruta: ").lower().replace("á", "a")
print(fruta_user)
peso = int(input("Escribe el peso: "))

frutas = { "platano": 1.35, "manzana": .80, "pera":.85, "naranja":.70 }

if fruta_user in frutas:   
        total = peso * frutas[fruta_user]
        print("El costo de %s es de %s" %(fruta_user, str(total)))
else:
        print("La fruta no existe.")
