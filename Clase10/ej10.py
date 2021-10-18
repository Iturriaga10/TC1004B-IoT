import random

clientes = [
    {
        "nif": 258,
        "nombre": "David Iturriaga",
        "direccion": "C29A",
        "telefono": 5539565536,
        "preferente": False
    },
    {
        "nif": 256,
        "nombre": "David Medina",
        "direccion": "C60C18",
        "telefono": 58529015428,
        "preferente": True
    },
    {
        "nif": 123,
        "nombre": "Almudena Moran",
        "direccion": "casa",
        "telefono": 5561155335,
        "preferente": False
    },
    {
        "nif": 450,
        "nombre": "Ana",
        "direccion": "Satelite",
        "telefono": 5512313555,
        "preferente": True
    },
    {
        "nif": 401,
        "nombre": "Carmen Tachica",
        "direccion": "C49A",
        "telefono": 5788823541,
        "preferente": True
    }
] 

def anadir_cliente():
    cliente = {
        "nif": random.randint(1,500),
        "nombre": raw_input("Introduce tu nombre: ").capitalize(),
        "direccion": raw_input("Introduce tu direccion: "),
        "telefono": int(raw_input("Introduce tu telefono: ")),
        "correo": raw_input("Introduce tu correo: "),
        "preferente": raw_input("Introduce si eres prefrente: ").lower() == "si",
    }
    clientes.append(cliente)

def eliminar_cliente():
    nif_cliente = int(raw_input("Que cliente desea eliminar: "))
    for x in clientes:
        if x["nif"] == nif_cliente:
            clientes.remove(x)

def mostrar_cliente():
    nif_cliente = int(raw_input("Que cliente quieres revisar: "))
    for x in clientes:
        if x["nif"] == nif_cliente:
            print(x)

def mostrar_clientes():
    print(clientes)

def mostrar_clientes_preferentes():
    clientes_preferentes = []
    for x in clientes:
        if x["preferente"] == True:
            clientes_preferentes.append(x)
    print(clientes_preferentes)


continuar = True
while continuar:
    accion = int(raw_input("1) Anadir Cliente \n2) Eliminar Cliente \n3) Mostrar Cliente \n4)Listar todos los Cliente \n5)Listar Clientes preferentes \n6) Terminar\n\n Selecciona la opcion:"))

    if accion == 1:
        anadir_cliente()
    elif accion == 2:   
        eliminar_cliente()
    elif accion == 3:
        mostrar_cliente()
    elif accion == 4:
        mostrar_clientes()
    elif accion == 5:
        mostrar_clientes_preferentes()
    elif accion == 6:
        continuar = False
    else:
        print("La opcion no esta disponible.")