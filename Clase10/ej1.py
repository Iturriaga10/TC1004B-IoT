divisa = {'Euro':'E', 'Dollar':'S', 'Yen':'Y'} # key: Value

divisa_usuario = raw_input("Escribe una divisa: ").lower()


for x in divisa:
    if x.lower() == divisa_usuario:
        print("El %s si existe y este es su moneda %s " %(x.lower(), divisa[x]))
