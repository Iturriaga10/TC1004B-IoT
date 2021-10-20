"""Ejercicio 6
Escribe un algoritmo que verifique si una persona puede obtener su licencia de conducir. Para 
hacerlo debe ser mayor de edad (18 años o más) y traer una identificación oficial."""


def confirmacion(edad):
    if edad < 18:
        print("Espera a que cumplas 18.")
    else:
        id = input("Traes tu identificacion oficial: ")
        if id == "si":
            print("Tramitando")
        else:
            print("Trae tu credencial.")


edad = int(input("Escriba su edad: "))
confirmacion(edad)
