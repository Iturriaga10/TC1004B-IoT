'''
Ejercicio 5
Escribir un programa que almacene el diccionario con los créditos de las asignaturas 
de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla 
los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, 
donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. 
Al final debe mostrar también el número total de créditos del curso.
 
'''

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