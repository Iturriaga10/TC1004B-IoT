loteria = []

for i in range(6):
    loteria.append(int(raw_input("Introduce el numero ganador: ")))

loteria.sort()

print("Los numeros ganadores son "+ str(loteria))