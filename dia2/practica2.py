palabra1 = input("Enter the first word: \n")
palabra2 = input("Enter the last word: \n")

lista1 = sorted(list(palabra1.lower()))
lista2  = sorted(list(palabra2.lower()))

if lista1 == lista2:
    print("Palindromo pa")
else:
    print("no invente chito")