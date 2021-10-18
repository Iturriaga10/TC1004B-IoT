cantidad = float(raw_input("Ingrese la cantidad a invertir: "))
interes = float(raw_input("Ingrese el interes anual: "))
anos = int(raw_input("Cuantos anos: "))

for w in range(1, anos+1):
    cantidad *= 1 + interes / 100
    #cantidad = cantidad * 1 interes / 100
    print("Capital tras %s anos: %s" %(str(w), str(round(cantidad,2))))