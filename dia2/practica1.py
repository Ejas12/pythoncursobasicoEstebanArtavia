
palabra = input("Enter the word: \n")

listaR = list(palabra.lower())
listaL  = listaR[::-1]

if listaL == listaR:
    print("es un Anagrama bicho")
else:
    print("no Batee mop")






