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
