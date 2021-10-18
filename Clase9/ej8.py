palabra = list(raw_input("introduce una palabra: "))

if palabra[::-1] == palabra:
    print("Palindromo")
else:
    print("No es Palindromo")
