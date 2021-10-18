num = int(raw_input("Introduce un numero positivo mayor que 2: "))

for i in range(2, num):
    if num % i == 0:
        break

if (i+1) == num:
    print("Es primo.")
else:
    print("No es primo.")