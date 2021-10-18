materias = ["Matematicas", "Fisica", "Quimica", "Historia",  "Lengua"]

reprobadas = []

for materia in materias:
    calificacion = float(raw_input("Cual es tu calificacion en " + materia + ": "))
    if calificacion <= 5:
        reprobadas.append(materia)

text="Usted reprobo: "
for reprobada in reprobadas:
    text+= reprobada + ", "

print(text)
