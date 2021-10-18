from urllib import request
import ssl

def palabras(url, user_pais):
    context = ssl._create_unverified_context()
    try:
        file = request.urlopen(url, context=context)
    except:
        return("LA URL no existe")
    else:
        
        contenido = file.read().decode('utf-8').split("\n")
        contenido.pop(0)
        
        paises = { }
        for linea in contenido:
            geolocalizacion = linea.split("\t")
            pais = geolocalizacion[0].split(",")
            paises.setdefault(pais[2], geolocalizacion[1:])
            
        año = 2000
        if user_pais in paises:
            texto = ""
            for y in paises[user_pais]:
                texto += str(año) + " - " + y + "\n"
                año += 1  
            return texto
        else:
            return ("Pais seleccionado, no existe.")

condicional = True
while condicional:
    user_pais = input("Escribe las iniciales de un pais europeo: ").upper()
    if user_pais == "SALIR":
        condicional = False
    else:
        print(palabras("https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true", user_pais))