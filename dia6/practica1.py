erick = {"Carlos", "Juan", "Maria", "Pedro", "Miguel"}
wife_hates = {"Ana", "Sofia", "Carlos"}
wife = {"Cindy", "Juan", "Miguel"}
#concenso
concenso = erick & wife
print (concenso)
#nombres de personas eric quiere y wife odia
excludedbywife = erick & wife_hates
#lista completa
completa = erick | wife
print (completa)
#### lista final
final = (erick | wife) - wife_hates
print (final)

a = ['grapes', 'melon', 'orange']
b = ['grapes', 'melon', 'apples']

def returnNomatches(a, b):
    a = set(a)
    b = set(b)
    return [list (b-a), list(a-b)]
returnNomatches(a,b)


agenda_tel = {
'Juan':87984512,
'Carlos':781247,
'Esteban':89910903
}
agenda_tel2 = {
'Juan2':87984512,
'Carlos2':781247,
'Esteban2':89910903
}

agenda_tel['Carlos']
#### agregar llave
agenda_tel['Guido'] = '22197385'
###sacar llave y si no encuentra, return none
agenda_tel.get('sofia', None)
#listar las llaves de un diccionario
list(agenda_tel)
#listar los valores 
list(agenda_tel.values())
#consultar si un key existe
'guido' in agenda_tel
#consultar si un value existe
89910903 in agenda_tel.values()

#crear dict desde una lista y formula
{x:x**2 for x in (2,4,6)}

#dic de tuplas
dict([("jose", 8991), ('esteban', 09003)])

#crear keys dict empty
keys = {'a','e','i','o','u'}
vowels = dict.fromkeys(keys)
#crear keys con un valor especifico

keys = {'a','e','i','o','u'}

vowels = dict.fromkeys(keys, 'vowel')

###
keys = {'a','e','i','o','u'}
value = [1]
vowels = dict.fromkeys(keys, value)
value.append([2])

###zip alinea listas juntas"
a = [1,2,3,4]
b = [3,4,5,6]
zip(a,b) ### se puede tirar a un dict, o una lista de tuplas

###agregar una llave o actualizar una existente
agenda_tel.update({'Carlos': 7777})

keys = list(agenda_tel)
values = list(agenda_tel.values())
keys2 = list(agenda_tel2)
values2 = list(agenda_tel2.values())
keyfinal = keys+keys2
valuesfinal = values+values2

###unir dos dicts, el doble * expande el dictinario en parejas tuples (KEY, Value)
dict(**agenda_tel, **agenda_tel2)


pass