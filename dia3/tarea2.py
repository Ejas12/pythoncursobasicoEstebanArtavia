####ejercicio1###
# Crear líneas de código en Python que calcule el promedio de los valores contenidos en una lista.#####

myvalues = [5,1,2,3,8,12]

average = sum(myvalues)/len(myvalues)

print("Promedio de los numeros es %.2f" % average)


#####Ejercicio 2###
# Escriba un código en python que determine cual grupo de personas contiene la mayor de todas las alturas de todas las personas#########

todos = [

[177,145,167,190,140,150,180,130], # grupo 1

[165,176,145,189,170,189,159,190], # grupo 2

[145,136,178,200,123,145,145,134], # grupo 3

[201,110,187,175,156,165,156,135] # grupo 4

]
maxofmax = 0
countindex = 0
for group in todos:
    countindex = countindex+1
    maxingroup = max(group)
    if maxingroup > maxofmax:
        maxofmax = maxingroup
        maxindex = countindex

    else:
        pass

print ("El mas alto es %d del grupo %d " %(maxofmax, maxindex))