num_word = int(input("Por Favor ingrese numero de palabras que quiere guardar:\n"))
counter = 1
listapalabras = []
foundword = []
while counter <= num_word:
    wordtext = str(input("Ingrese palabra %d: \n" %counter))
    counter= counter+1
    listapalabras.append(wordtext)
print("La lista de Palabras es %s:\n" %listapalabras)

searchstr = input('Que palabra quiere Sustituir?\n')

replaceby = input('Por cual palabra?\n')
try:
    indexno = listapalabras.index(searchstr)
    listapalabras[indexno] = replaceby
    print ("La lista ahora es %s:\n" %listapalabras)
except:
    print("La lista no contiene la palabra solicitada")

