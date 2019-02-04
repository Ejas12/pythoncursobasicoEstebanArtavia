num_word = int(input("Por Favor ingrese numero de palabras que quiere guardar:\n"))
counter = 1
listapalabras = []
foundword = []
while counter <= num_word:
    wordtext = str(input("Ingrese palabra %d: \n" %counter))
    counter= counter+1
    listapalabras.append(wordtext)
print("La lista de Palabras es %s:\n" %listapalabras)

searchstr = input('Que palabra quiere Remover?\n')

try:
    listapalabras.remove(searchstr)
    print ("La lista ahora es %s:\n" %listapalabras)
except:
    print("La lista no contiene la palabra solicitada")

pass