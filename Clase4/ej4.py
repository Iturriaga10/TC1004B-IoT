"""Ejercicio 4
Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe 
recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%."""


def factura(cantidad, iva=21):
    return cantidad * (1 + (iva / 100))


cantidad = float(input("Introduzca la cantidad en pesos: "))
iva = float(input("Introduzca el porcentaje de IVA: "))

print(factura(cantidad, iva))
