numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Solucion 1
 reversa=""
 for i in range(1, 11):
     reversa+=str(numeros[-i])+ ", "

 print(reversa)

# Solucion 2
numeros.reverse()

reversa=""
for numero in numeros:
    reversa+=str(numero)+ ", "

print(reversa)
