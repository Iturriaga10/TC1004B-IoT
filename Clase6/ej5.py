def mayuscula(nombre):
    return nombre.upper()

def minuscula(nombre):
    return nombre.lower()

def capital(nombre):
    return nombre.capitalize()

nombre = raw_input("Escribe tu nombre: ")
print(mayuscula(nombre))
print(minuscula(nombre))
print(capital(nombre))
