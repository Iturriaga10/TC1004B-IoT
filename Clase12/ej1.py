numero = raw_input("Introduce un numero del 1 al 10: ")

# w (write)
# r (read)
f = open("tabla-" + numero + ".txt", 'w')

for i in range(1, 11):
    # .read() --> Escribir información en el fichero.
    f.write(str(i) + " x " + numero + " = " + str(i * int(numero)) + "\n")
f.close()
