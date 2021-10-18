facturas = {} 

def crear_factura():
    nueva_factura = raw_input("Introduce el numero de la factura y el monto separados por una coma: ").lower().split(",")
    facturas.setdefault(nueva_factura[0], nueva_factura[1])# Agrega nuevos elementos a un diccionario.

def pagar_factura():
    factura = raw_input("Introduce el numero de la factura: ")
    if factura in facturas:
        facturas.pop(factura) # Eliminar un elemento de un diccionario.
    else:
        print("La factura no existe.")

continuar = True
while continuar:
    accion = int(raw_input("1) Crear Factura \n2) Pagar Factura \n3)Terminar  \n Selecciona la opcion:"))

    if accion == 1:
        crear_factura()
    elif accion == 2:   
        pagar_factura()
    elif accion == 3:
        continuar = False
    else:
        print("La opcion no esta disponible.")