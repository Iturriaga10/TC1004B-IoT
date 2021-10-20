'''
Ejercicio 7
El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las 
siguientes columnas: Nombre (nombre de la empresa), Final (precio de la acción al cierre 
de bolsa), Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo 
de la acción durante la jornada), Volumen (Volumen al cierre de bolsa), Efectivo 
(capitalización al cierre en miles de euros).
Construir una función reciba el fichero de cotizaciones y devuelva un diccionario con los 
datos del fichero por columnas.
Construir una función que reciba el diccionario devuelto por la función anterior y cree 
un fichero en formato csv con el mínimo, el máximo y la media de dada columna.
'''

def preprocesado(ruta):
    try:
        f = open(ruta, 'r')
    except:
        print("El fichero no existe")
        return

    lineas = f.readlines()
    f.close()

    claves = lineas[0].replace("\n", "").split(";")
    
    valores = lineas[1:]

    cotizacion = {}
    for valor in valores:
        valor_linea = valor.replace("\n", "").split(";")

        dato_cotizacion = {}
        for x in range(1, 6):
            dato_cotizacion.setdefault(claves[x], valor_linea[x])
        
        cotizacion.setdefault(valor_linea[0], dato_cotizacion)
    
    return(cotizacion)

def resumen(ruta, cotizaciones):
    f = open(ruta, 'w')
    f.write("Nombre;Final;Máximo;Mínimo\n")
    
    for cotizacion in cotizaciones:
        texto = cotizacion + ";" + cotizaciones[cotizacion]["Final"] + ";" + cotizaciones[cotizacion]["Máximo"] + ";" + cotizaciones[cotizacion]["Mínimo"] + "\n"
        f.write(texto)

    f.close()

cotizaciones = preprocesado('cotizacion.csv')
resumen('resumen_cotizaciones.csv', cotizaciones)