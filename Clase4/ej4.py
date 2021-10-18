def factura(cantidad, iva=21):
    return cantidad * (1 + (iva / 100))

cantidad = float(raw_input("Introduzca la cantidad en pesos: "))
iva = float(raw_input("Introduzca el porcentaje de IVA: "))

print(factura(cantidad, iva))