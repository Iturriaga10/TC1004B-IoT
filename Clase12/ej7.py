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