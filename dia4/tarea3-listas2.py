num_word = int(input("Por Favor ingrese numero de palabras que quiere guardar:\n"))
counter = 1
listapalabras = []
foundword = []
while counter <= num_word:
    wordtext = str(input("Ingrese palabra %d: \n" %counter))
    counter= counter+1
    listapalabras.append(wordtext)
print("La lista de Palabras es %s:\n" %listapalabras)

searchstr = input('Que palabra quiere buscar?\n')

for palabra in listapalabras:
    if searchstr in palabra:
        foundword.append(palabra)

cantidad = len(foundword)

if cantidad == 0:
    print("La palabra no esta en la lista")
else: 
    print ("Se encontro la palabra %s veces" %cantidad)