'''
 Escribir un programa que guarde en una variable el diccionario 
 {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su 
 símbolo o un mensaje de aviso si la divisa no está en el diccionario.
'''
divisa = {'Euro':'E', 'Dollar':'S', 'Yen':'Y'} # key: Value

divisa_usuario = raw_input("Escribe una divisa: ").lower()


for x in divisa:
    if x.lower() == divisa_usuario:
        print("El %s si existe y este es su moneda %s " %(x.lower(), divisa[x]))
