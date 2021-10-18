import math

def circulo(radio):
    return math.pi * radio ** 2

def cilindro(radio, altura):
    return circulo(radio) * altura

print(cilindro(3, 5))