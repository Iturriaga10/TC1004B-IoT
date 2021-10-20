'''
Ejercicio 9
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
Las facturas se almacenarán en un diccionario donde la clave de cada factura será el 
número de factura y el valor el coste de la factura. El programa debe preguntar al 
usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea 
añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá 
al diccionario. Si se desea pagar una factura se preguntará por el número de factura y 
se eliminará del diccionario. Después de cada operación el programa debe mostrar por 
pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
'''

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