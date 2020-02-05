class linha:

    def __init__(self, cord1, cord2):

        self.cord1 = cord1
        self.cord2 = cord2
    
    def Distancia(self):
        dist = ((self.cord2[0]-self.cord1[0])**2 + (self.cord2[1]-self.cord1[1])**2)**(0.5)
        print(dist)
    
    def Angulo(self):
        angulo = (self.cord2[1]-self.cord1[1])/(self.cord2[0] - self.cord1[0])
        print (angulo)
    
coordenada1 = (3,2)
coordenada2 = (8,10)

linha1 = linha(coordenada1,coordenada2)

linha1.Distancia()
linha1.Angulo()


class cilindro:

    pi = 3.14
    def __init__(self, altura=1, raio=1):
        self.altura=altura
        self.raio=raio
    
    def Volume(self):
        vol = self.pi * self.raio**2 * self.altura
        print(vol)

    def AreaSuperficial(self):
        Al = 2 * self.pi * self.raio * self.altura
        Ab = self.pi * self.raio**2
        print(Al + 2*Ab)

cil = cilindro(2,3)

cil.Volume()
cil.AreaSuperficial()
