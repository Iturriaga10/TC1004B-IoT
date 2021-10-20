"""Ejercicio 6
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde."""


hours = input("Ingrese las horas trabajadas: ")
amount = input("Ingrese el coste por hora: ")
paga = float(hours) * float(amount)
print("La paga seria de: " + str(paga))
