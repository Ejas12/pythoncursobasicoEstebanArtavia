class CalculadoraBasica:
    def suma(self):
        sumatoria = int(self.numero1)+int(self.numero2)
        print("La suma de {0}+{1} es {2}".format(self.numero1,self.numero2,sumatoria))
    def resta(self):
        resta = int(self.numero1)-int(self.numero2)
        print("La resta de {0}-{1} es {2}".format(self.numero1,self.numero2,resta))
    def producto(self):
        multi = int(self.numero1)*int(self.numero2)
        print("La multiplicacion de {0}*{1} es {2}".format(self.numero1,self.numero2,multi))
    def frac (self):
        fraccion = int(self.numero1)/int(self.numero2)
        print("La division de {0}/{1} es {2}".format(self.numero1,self.numero2,fraccion))
    def __init__(self):
        self.operator = input("Hola, ingrese la operacion que requiere ejecutar:\nx:multiplicacion,+:suma,-:resta y div:division\n")
        self.numero1 = input("Ingrese el primer numero:\n")
        self.numero2 = input("Ingrese el segundo numero:\n")
        if self.operator == "x":
            self.producto()
        elif self.operator == '+':
            self.suma()
        elif self.operator == '-':
            self.resta()
        elif self.operator == 'div':
            self.frac()
        else:
            print ("Por Favor escoja una operacion valida")
            self.__init__()

instanciadecalcu = CalculadoraBasica()

