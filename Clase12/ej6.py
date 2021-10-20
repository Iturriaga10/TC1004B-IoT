'''
Ejercicio 6
Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos 
de los clientes de una empresa. El programa incorporar funciones crear el fichero con el 
listín si no existe, para consultar el teléfono de un cliente, añadir el teléfono de un 
nuevo cliente y eliminar el teléfono de un cliente. El listín debe estar guardado en el 
fichero de texto listin.txt donde el nombre del cliente y su teléfono deben aparecer 
separados por comas y cada cliente en una línea distinta.
'''

file_name = "listin.txt"

def agregar_numero():
    nombre = input("Escribir su nombre: ")
    telefono = int(input("Escribir su telefono: "))

    f = open(file_name, "a")
    f.write(nombre + "," + str(telefono) + "\n")
    f.close()

def eliminar_numero():
    user_nombre = input("Escribir el nombre que deseas eliminar: ")
    f = open(file_name, "r")
    lineas = f.readlines()
    f.close()

    existe = False
    for x in range(0, len(lineas)):
        nombre  = lineas[x].split(",") ["David", 78979879]
        if nombre[0] == user_nombre:
            lineas.pop(x)
            break
        else:
            existe = True
    
    if existe:
        print("El contacto no existe.")
    
    f = open(file_name, "w")
    for linea in lineas:
        f.write(linea)

def listar_numero():
    f = open(file_name, "r")
    lineas = f.readlines()
    f.close()
    
    texto = ""
    for linea in lineas:
        texto += linea.replace(",", " - ") 
    
    print(texto)


condicional = True
while condicional:
    opcion = int(input("1) Agregar contacto \n2) Eliminar contacto \n3) Listar contactos. \n4) Salir \n\nEscribe la opcion indicada: "))
    if opcion == 1:
        agregar_numero()
    elif opcion == 2:
        eliminar_numero()
    elif opcion == 3:
        listar_numero()
    elif opcion == 4:
        condicional = False    
    else:
        print("Opcion Invalida")