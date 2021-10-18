'''
Ejercicio 3
Escribir una función que pida dos números n y m entre 1 y 10, 
lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, 
y muestre por pantalla la línea m del fichero. Si el fichero no existe 
debe mostrar un mensaje por pantalla informando de ello.
'''

numero_n = input("Introduce un numero del 1 al 10: ")
numero_m = int(input("Introduce un numero del 1 al 10: "))

# w (write)
# r (read)
try:
    f = open("tabla-" + numero_n + ".txt", 'r')
except:
    print("El fichero no existe")
else:    
    # .readlines() --> Lee la información del fichero y lo guarda en un arreglo, separandolo por saltos de linea. 
    lineas = f.readlines()
    print(lineas[numero_m-1])
