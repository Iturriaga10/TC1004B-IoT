name = raw_input("Escriba su nombre: ")
sex = raw_input("Escriba su sexo: ")

first_letter = name[0].lower() #Patricio

# AND / OR / NOT

if first_letter < "m" and sex == "mujer":
    print(" Pertences al grupo A")
elif first_letter > "m" and sex == "mujer":
    print(" Pertences al grupo B")
elif first_letter < "n" and sex == "hombre":
    print(" Pertences al grupo A")
elif first_letter > "n" and sex == "hombre":
    print(" Pertences al grupo B")
else:
    print("Escribe bien, hombre o mujer en el sexo.")