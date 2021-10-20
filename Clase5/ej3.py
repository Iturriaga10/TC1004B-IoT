"""Ejercicio 3
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el 
divisor es cero el programa debe mostrar un error."""

num1 = float(input("Escriba un numero: "))
num2 = float(input("Escriba otro numero: "))

if num2 != 0:
    div = num1 / num2
    # print("El resultado de la division es: %s" %str(div))
    print("El resultado de la division es: " + str(div))
else:
    print("Error")
