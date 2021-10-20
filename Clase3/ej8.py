"""Ejercicio 8
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el 
índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice 
de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos 
decimales."""

weight = float(input("Introduce tu peso en kilogramos: "))
height = float(input("Introduce tu estatura en metros: "))
imc = (weight / (height ** 2))
print("Tu imc es " + str(round(imc)))
