numero = int(raw_input("Escriba un numero entero positivo: "))

out = ""
for y in range(numero, -1, -1):
    out += str(y) + ", " # out = out + str(y) + ", "

print(out)

