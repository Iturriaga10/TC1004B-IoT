palabra = raw_input("Introduce una palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u']

for vocal in vocales:
    veces =  0
    for letra in palabra:
        if letra == vocal:
            veces+=1
    print("La vocal " + vocal + " aparece " + str(veces) + " veces")