class Animal ():

    def __init__(self):

        self.Color = input("\tDigita el color: ")
        self.Peso = float(input("\tDigita el peso en Kg: "))

    def Comer (self):
        
        return "Está comiendo"

    def Moverse(self):

        return "Camina en"


class Ave(Animal):

    def __init__(self):
        print("Ave:")
        super().__init__()
        self.Tipo = input("\tDigite el tipo de ave: ")
    
    def Volar(self):
        print("\tEl",self.Tipo," de color",self.Color," con un peso de ",self.Peso," Kg ",super().Comer()," y ",super().Moverse()," 2 patas y también puede volar")

class Perro(Animal):

    def __init__(self):
        print("Perro: ")
        super().__init__()
        self.Raza = input("\tDigite la raza del perro :")

    
    def Ladrar (self):
        print("\tEl",self.Raza," de color",self.Color," con un peso de ",self.Peso," Kg ",super().Comer()," y ",super().Moverse()," 4 patas y hace !WUAF WUAFFFFFF!")

ave = Ave()
ave.Volar()
perro = Perro()
perro.Ladrar()
