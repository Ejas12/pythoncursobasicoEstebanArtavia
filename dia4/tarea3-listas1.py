num_word = int(input("Por Favor ingrese numero de palabras que quiere guardar:"))
counter = 1
listapalabras = []

while counter <= num_word:
    wordtext = str(input("Ingrese palabra %d" %counter))
    counter= counter+1
    listapalabras.append(wordtext)

print("La lista de Palabras es %s" %listapalabras)

guess = int(input("Digame cuantas palabras tiene la lista?"))

if guess == len(listapalabras):
    print("Bien dicho bicho!!")
else:
    print("No batee!!")



 
