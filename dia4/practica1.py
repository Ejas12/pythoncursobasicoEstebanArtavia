class Animal:
    def __init__(self, pat, ojo, nom):
        self.pat = pat
        self.ojo = ojo
        self.nom = nom
        self.eat = 0
    def comer (self, comida):
        self.eat = self.eat+comida
    


class Planta:
    def __init__(self, alt, color, frutos):
        self.alt = int(alt)
        self.color = color
        self.frutos = frutos
    def  crecer (self, crecer):
        self.alt = self.alt+crecer


perro = Animal(4, 2, 'firulais')
petunia = Planta(5,"Rojo",2)
pass