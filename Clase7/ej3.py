numero = int(raw_input("Escriba un numero entero positivo: "))

out = ""
for y in range(1, numero + 1, 2):
    out += str(y) + ", " # out = out + str(y) + ", "

print(out)

