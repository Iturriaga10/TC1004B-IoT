num = int(raw_input("Introduce un numero positivo mayor que 2: "))

i = 2
while num % i != 0:
    i += 1

if i == num:
    print("Es primo.")
else:
    print("No es primo.")