def confirmacion(edad):
    if edad < 18:
        print("Espera a que cumplas 18.")
    else:
        id = raw_input("Traes tu identificacion oficial:")
        if id == "si":
            print("Tramitando")
        else:
            print("Trae tu credencial.") 

edad = int(raw_input("Escriba su edad:"))
confirmacion(edad)