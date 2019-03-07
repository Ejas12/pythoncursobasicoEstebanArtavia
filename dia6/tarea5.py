class Paciente:
    def __init__(self, nombrep, apellidop, telp, dirp, enfermedades, medicamentosp):
        self.nombrep = nombrep
        self.apellidop = apellidop
        self.telp = telp
        self.dirp = dirp
        self.enfermedades = enfermedades
        self.medicamentosp = medicamentosp
    def formattotable(self):
        self.pacientedict = {'Nombre':self.nombrep,'Apellido':self.apellidop,'Telefono':self.telp,'Direccion':self.dirp,'Enfermedades':self.enfermedades,'Medicamentos':self.medicamentosp}
        return(self.pacientedict)
    

tablepaciente = []
def pacienteaddition(inputdict):
    tablepaciente.append(inputdict)


pass

paciente1 = Paciente('Pablo','Jara','89910903','Heredia',['Conjuntivitis', 'Gonorrea', 'Tetatnos'],['tiamina','crema de rosas'])
paciente2 = Paciente('Pedro','Bautista','89910302','Alajuela',['Rabia', 'Prolapso rectal', 'Escorbuto'],['peptobismol'])
paciente3 = Paciente('Anselmo','Mendez','89914320','San Jose',['Resfriado','Hipertension','Asma'],['antutifludes'])
paciente4 = Paciente('Plutarco','Arce','21401012','La Carpio',['Cancer de prostata'],['ibuprofeno'])
pacienteaddition(paciente1.formattotable())
pacienteaddition(paciente2.formattotable())
pacienteaddition(paciente3.formattotable())
pacienteaddition(paciente4.formattotable())

def askfornewpatient():
    nombrepaciente = input("Nombre del paciente:\n")
    apellidopaciente= input("Apellido del paciente:\n")
    telpaciente= input("Telefono del paciente:\n")
    dirpaciente= input("Direccion del paciente")
    enfermedades = []
    masenferemedades = 'Y'
    while masenferemedades == 'Y':
        enfermedades.append(input("Nombre de la enfermedad:\n"))
        masenferemedades = (input("Alguna otra?\n Y o N:")).upper()
    masmedicamnetos = 'Y'
    medicamentos = []
    while masmedicamnetos == 'Y':
        medicamentos.append(input("Nombre del medicamento?\n"))
        masmedicamnetos = (input("Alguna otra?\n Y o N:")).upper()
    pacientecard = Paciente(nombrepaciente, apellidopaciente, telpaciente, dirpaciente, enfermedades, medicamentos)
    pacienteaddition(pacientecard.formattotable())

def deletepaciente (id):
    deleteditem = tablepaciente.pop(id)
    print("Paciente borrado es {}".format(deleteditem.__str__()))

def agregarmeds (id):
    masmedicamnetos = 'Y'
    while masmedicamnetos == 'Y':
        tablepaciente[id]['Medicamentos'].append(input("Nombre del medicamento?\n"))
        masmedicamnetos = (input("Alguna otra?\n Y o N:")).upper()
def agregarenf (id):
    masenf = 'Y'
    while masenf == 'Y':
        tablepaciente[id]['Enfermedades'].append(input("Nombre de la enfermedad?\n"))
        masenf = (input("Alguna otra?\n Y o N:")).upper()    

def findpatient (id=None, Nombre=None, Apellido=None):
    if id != None:
        foundpatient = tablepaciente[id]
    elif id == None and Nombre !=None:
        foundpatient = [d for d in tablepaciente if d['Nombre'] == Nombre]
    elif id == None and Nombre ==None and Apellido !=None:
        foundpatient = [d for d in tablepaciente if d['Apellido'] == Apellido]
    return(foundpatient)

def reportenfermedades ():
    enfermedades = [d['Enfermedades']) for d in tablepaciente]




           



# turn to dict: dicpacientes = {i: tablepaciente[i] for i in range(0,len(tablepaciente))}
pass
        

pass

#def selectpacientes:
    


#def agregarpaciente:


    
    

