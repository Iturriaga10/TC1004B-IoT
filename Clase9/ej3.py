materias = ["Matematicas", "Fisica", "Quimica", "Historia",  "Lengua"]

calificaciones = []

for materia in materias:
    calificacion = float(raw_input("Cual es tu calificacion en " + materia + ": "))
    calificaciones.append(calificacion)

for i in range(len(materias)):
     print("En " + materias[i] + " saque: " + str(calificaciones[i]))
