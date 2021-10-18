longitud = raw_input("Ingrese la longitud en metros: ")

conv_foot = ((float(longitud) * 100) / 2.5) / 12
# conv_cm = float(longitud) * 100 
# conv_inch = conv_cm / 2.5
# conv_foot = conv_inch / 12
print("El resultado en pies es: " + str(conv_foot))