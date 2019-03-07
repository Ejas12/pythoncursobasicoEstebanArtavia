import csv

input_file = csv.DictReader(open("C:\\Users\\Esteban Artavia\\Documents\\scripts\\\Pythoncourse\\dia7\\serverdatabase.csv"))
outputfile = open('C:\\Users\\Esteban Artavia\\Documents\\scripts\\\Pythoncourse\\dia7\\output.txt', 'w+')
outputfile.write('NEW RUN\n')
outputfile.close
outputfile = open('C:\\Users\\Esteban Artavia\\Documents\\scripts\\\Pythoncourse\\dia7\\output.txt', 'a+')
for lineausuario in input_file:
    nombre = lineausuario['first_name']
    apellido = lineausuario['last_name']
    numero = lineausuario['phone1']
    mail = lineausuario['email'].split('@')
    login = mail[0]
    proveedorurl = mail[1].split('.')[0]

    pass
    mensaje_print = "Hola me llamo {nombre} {apellido}. Mi teléfono es {numero} .Mi usuario de correo es: {login} usando una cuenta de {proveedorurl}\n".format(nombre = nombre, apellido = apellido, numero = numero, login = login, proveedorurl = proveedorurl)
    outputfile.writelines(mensaje_print)
