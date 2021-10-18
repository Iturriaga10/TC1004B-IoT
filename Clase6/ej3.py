import math

def vector(x, y):
    return math.sqrt(x ** 2 + y ** 2)

x = float(raw_input("Escribe el valor de x: "))
y = float(raw_input("Escribe el valor de y: "))

print("El modulo es: " + str(vector(x,y)))