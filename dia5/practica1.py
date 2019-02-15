class Animal:
    contar_animales = 0
    def __init__(self):
        print("Creando Animal.....")
        self.vivo = True
        self.crecer = 1
        self.respirar = True
        self.reproducir = "not yet"
        self.Morir = False



class Pato(Animal):
    def __init__(self, nombre_pato = 'pato'):
        super().__init__()
        self.nombre_pato = nombre_pato
        print("Creando Pato....")
    def __str__(self):
        return(self.nombre_pato)
    def __repr__
        

donal = Pato()

pass  
