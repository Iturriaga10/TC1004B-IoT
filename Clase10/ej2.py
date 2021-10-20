'''
Ejercicio 2
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y 
lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> 
tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
'''

persona = { "nombre": raw_input("Escribe tu nombre: "), 
            "edad": int(raw_input("Escribe tu edad: ")), 
            "direccion": raw_input("Escribe tu direccion: "), 
            "telefono": int(raw_input("Escribe tu telefono: ")) }

# print(persona)

print(persona["nombre"] + " tiene " + str(persona["edad"]) + 
      " anos, vive en " + persona["direccion"] + 
      " y su numero de telefono es " + str(persona["telefono"]))