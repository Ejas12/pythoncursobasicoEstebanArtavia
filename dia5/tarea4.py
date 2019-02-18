import random, math
###master class###
class Vehiculo:
    def __init__(self):
        self.fuerza_motor = random.randint(1,9)
        self.avancetotal = 0
        self.win = False
        self.modelo = 'Nada'
    def metaalcanzada (self):
        if self.avancetotal >= 1000:
            print ("El Vehiculo {} ha ganado".format(self.modelo))
            self.win = True
    def fuerza_motorfunc (self):
        self.fuerza_motor = random.randint(1,9)



###subclasses####
class Camion(Vehiculo):
    def __init__(self, modelo='Toyota'):
        super().__init__()
        self.modelo = modelo
        self.avance = self.fuerza_motor*2+1
        self.tipo = "Camion"
        self.avancetotal = self.avancetotal+self.avance
    def metaalcanzada(self):
        super().metaalcanzada()
    def avanzar(self):
        self.avance = self.fuerza_motor*2+1
        self.avancetotal = self.avancetotal+self.avance
    
class Tractor(Vehiculo):
    def __init__(self, modelo='Toyota'):
        super().__init__()
        self.modelo = modelo
        self.avance = int(math.log(self.fuerza_motor, 2))
        self.tipo = "Tractor"
        self.avancetotal = self.avancetotal + self.avance
    def metaalcanzada(self):
        super().metaalcanzada()
    def avanzar(self):
        self.avance = int(math.log(self.fuerza_motor, 2))
        self.avancetotal = self.avancetotal + self.avance

class Sedan(Vehiculo):
    def __init__(self, modelo = 'Toyota'):
        super().__init__()
        self.modelo = modelo
        self.avance = 3*self.fuerza_motor**2
        self.avancetotal = self.avancetotal +self.avance
        self.tipo = "Sedan" 
    def metaalcanzada(self):
        super().metaalcanzada()
    def avanzar(self):
        self.avance = 3*self.fuerza_motor**2
        self.avancetotal = self.avancetotal + self.avance
class Bus(Vehiculo):
    def __init__(self, modelo = "Toyota"):
        super().__init__()
        self.modelo = modelo
        self.avance = 5*self.fuerza_motor
        self.avancetotal = self.avancetotal+self.avance
    def avanzar(self):
        self.avance = 5*self.fuerza_motor
        self.avancetotal = self.avancetotal+self.avance



###functions#####
def carrera (camion, tractor, sedan, bus, *args):
    ciclos = 0
    carrera_terminada = False
    while carrera_terminada != True:
        camion.metaalcanzada()
        tractor.metaalcanzada()
        sedan.metaalcanzada()
        bus.metaalcanzada()
        ciclos = ciclos+1
        if camion.win == True or tractor.win == True or sedan.win == True or bus.win == True:
            print ("alcanzo la meta en {} ciclos".format(ciclos))
            carrera_terminada = True
        else:
            
            camion.fuerza_motor()
            camion.avanzar()
            tractor.avanzar()
            sedan.avanzar()
            bus.avanzar()



    





newcamion = Camion("susuki")
newtractor = Tractor("chapulin")
newsedan = Sedan("centra")
newbus = Bus('volvo')

carrera(newcamion, newtractor, newsedan, newbus)

pass

