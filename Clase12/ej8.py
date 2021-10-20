'''
Ejercicio 8
El fichero calificaciones.csv contiene las calificaciones de un curso. Durante el curso 
se realizaron dos exámenes parciales de teoría y un examen de prácticas. Los alumnos que 
tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo en la al final del 
curso (convocatoria ordinaria). Escribir un programa que contenga las siguientes funciones:
Una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios, 
donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. 
La lista tiene que estar ordenada por apellidos.
Una función que reciba una lista de diccionarios como la que devuelve la función anterior y 
añada a cada diccionario un nuevo par con la nota final del curso. El peso de cada parcial 
de teoría en la nota final es de un 30% mientras que el peso del examen de prácticas es de 
un 40%.
Una función que reciba una lista de diccionarios como la que devuelve la función anterior 
y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. 
Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los 
exámenes parciales y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.
'''

def notas(ruta):
    try:
        f = open(ruta, 'r')
    except:
        print("El fichero no existe")
        return

    lineas = f.readlines()
    f.close()

    claves = lineas[0].replace("\n", "").split(";")
    
    valores = lineas[1:]
    
    calificaciones = {}
    for valor in valores:
        valor_linea = valor.replace("\n", "").split(";")

        dato_calificacion = {}
        for x in range(2, 9):
            dato_calificacion.setdefault(claves[x], valor_linea[x])
        
        calificaciones.setdefault(valor_linea[1], dato_calificacion)
    
    return(calificaciones)

def status_alumno(calificaciones):
    reprobados_inasistencia = {}
    acreditados = { }
    reprobados = { }

    # Reprobados por inassitencia
    for nombre in calificaciones:
        if int(calificaciones[nombre]["Asistencia"].replace("%", "")) < 75:
            reprobados_inasistencia.setdefault(nombre, calificaciones[nombre])

    # Acreditados
    for nombre in calificaciones:
        # Parciales
        parcial1 = float(calificaciones[nombre]["Parcial1"].replace(",", "."))
        parcial2 = float(calificaciones[nombre]["Parcial2"].replace(",", "."))
        
        # Ordinarios
        if calificaciones[nombre]["Ordinario1"] == "":
            ordinario1 = 0
        else:
            ordinario1 = float(calificaciones[nombre]["Ordinario1"].replace(",", "."))

        if calificaciones[nombre]["Ordinario2"] == "":
            ordinario2 = 0
        else:
            ordinario2 = float(calificaciones[nombre]["Ordinario2"].replace(",", "."))

        # Evaluar Calificación Mayor Parcial 1.
        if parcial1 >= ordinario1:
            max_1 = parcial1
        else:
            max_1 = ordinario1

        # Evaluar Calificación Mayor Parcial 2.
        if parcial2 >= ordinario2:
            max_2 = parcial2
        else:
            max_2 = ordinario2
        
        promedio_final = ((max_1 + max_2) / 2) * .6

        # Practicas
        if calificaciones[nombre]["Practicas"] == "":
            practicas = 0
        else:
            practicas = float(calificaciones[nombre]["Practicas"].replace(",", ".")) 

        # Ordinario Practicas
        if calificaciones[nombre]["OrdinarioPracticas"] == "":
            ordinario_practicas = 0
        else:
            ordinario_practicas = float(calificaciones[nombre]["OrdinarioPracticas"].replace(",", ".")) 

        # Evaluar Calificación Mayor Practicas.
        if practicas >= ordinario_practicas:
            max_3 = practicas
        else:
            max_3 = ordinario_practicas

        promedio_final_practicas = max_3 * .4

        total = promedio_final + promedio_final_practicas

        if total > 5:
            acreditados.setdefault(nombre, calificaciones[nombre])
        else:
            reprobados.setdefault(nombre, calificaciones[nombre])

    print("Reprobados Inasistencia")
    print(reprobados_inasistencia)
    print("Reprobados")
    print(reprobados)
    print("Aprobados")
    print(acreditados)
    
calificaciones = notas('calificaciones.csv')
status_alumno(calificaciones)
