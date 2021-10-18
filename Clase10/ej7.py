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




