'''
Ejercicio 4
Escribir un programa que acceda a un fichero de internet mediante su url y 
muestre por pantalla el número de palabras que contiene.
'''

from urllib import request
import ssl

def palabras(url):
    context = ssl._create_unverified_context()
    try:
        file = request.urlopen(url, context=context)
    except:
        return("LA URL no existe")
    else:
        content = file.read()
        return len(content.split())


print(palabras("https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true"))