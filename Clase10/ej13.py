
numeros =  raw_input("Introduce una lista de numero separados por comas: ").split(",")

total_media = 0
for numero in numeros:
    total_media += int(numero)

media = total_media / len(numeros)

total_dsv = 0
for numero in numeros:
    total_dsv += (int(numero) - media) ** 2 


print("media = " + str(media))
print("dv = " + str(total_dsv / len(numeros)))