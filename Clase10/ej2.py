# nombre = 
# edad = int(raw_input("Escribe tu edad: "))
# direccion = raw_input("Escribe tu direccion: ")
# telefono = int(raw_input("Escribe tu telefono: "))

persona = { "nombre": raw_input("Escribe tu nombre: "), 
            "edad": int(raw_input("Escribe tu edad: ")), 
            "direccion": raw_input("Escribe tu direccion: "), 
            "telefono": int(raw_input("Escribe tu telefono: ")) }

# print(persona)

print(persona["nombre"] + " tiene " + str(persona["edad"]) + 
      " anos, vive en " + persona["direccion"] + 
      " y su numero de telefono es " + str(persona["telefono"]))