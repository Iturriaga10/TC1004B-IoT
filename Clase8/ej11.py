word = raw_input("Introduzca una palabra: ")

# [ 0, 1, 2, 3]
# ["Hola"]

for i in range(len(word)-1, -1, -1):
    print(word[i])