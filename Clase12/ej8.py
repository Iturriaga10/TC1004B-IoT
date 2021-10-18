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
