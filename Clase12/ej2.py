'''
Ejercicio 2
Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt 
con la tabla de multiplicar de ese número, done n es el número introducido, y la muestre 
por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de 
ello. 
'''

numero = raw_input("Introduce un numero del 1 al 10: ")

# w (write)
# r (read)
try:
    f = open("tabla-" + numero + ".txt", 'r')
except:
    print("El fichero no existe")
else:    
    # .read() --> Lee la información del fichero. 
    print(f.read())
