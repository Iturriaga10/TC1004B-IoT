weight = float(raw_input("Introduce tu peso en kilogramos: "))
height = float(raw_input("Introduce tu estatura en metros: "))
imc = (weight / (height ** 2))
print("Tu imc es " + str(round(imc)))