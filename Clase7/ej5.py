"""Ejercicio 5
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número
de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la 
inversión."""

cantidad = float(input("Ingrese la cantidad a invertir: "))
interes = float(input("Ingrese el interes anual: "))
anos = int(input("Cuantos anos: "))

for w in range(1, anos+1):
    cantidad *= 1 + interes / 100
    # cantidad = cantidad * 1 interes / 100
    print("Capital tras %s anos: %s" % (str(w), str(round(cantidad, 2))))
