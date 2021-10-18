materias = {'Matematicas': 6, 'Fisica': 4, 'Quimica': 5}

# Solucion 1
texto = "David "
for materia in materias:
     texto +=  "tiene en " + materia + " " + str(materias[materia]) + ", "
print(texto)

# Solucion 2
texto = "David "
for i, j in materias.items():
    texto +=  "tiene en " + i + " " + str(j) + ", "

print(texto)