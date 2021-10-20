'''
Ejercicio 7
Escribir un programa que cree un diccionario simulando una cesta de la compra. 
El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta 
que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra 
y el coste total, con el siguiente formato
'''

articulos = [ { "Precio": 10.5, "Articulo": "1" },
              { "Precio": 20.6, "Articulo": "2"},
              { "Precio": 9.4,  "Articulo": "3"} ]

continuar = True
while continuar:
    user_art = {
        "Articulo": raw_input("Introduce el artiuculo: "),
        "Precio": float(raw_input("Introduce el costo: "))
    }
    articulos.append(user_art)
    continuar = raw_input("Desea Continuar: ").lower() == "si"

costo = 0
print("Articulo \t Precio")
for articulo in articulos:
    print(articulo["Articulo"] + "\t\t" + str(articulo["Precio"]))
    costo += articulo["Precio"]

print("Total" + "\t\t" + str(costo))