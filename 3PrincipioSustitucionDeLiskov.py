#Principio SOLID de Sustitucion de Liskov

class vehiculo():
    def __init__(numeroSillas):
        self.numeroSillas = numeroSillas

class Renault:
    def numeroSillas(self):
        return super().get_numeroSillas('5') 

class Audi:
    def numeroSillas(self):
        return super().get_numeroSillas('2') 

class Mercedes:
    def numeroSillas(self):
        return super().get_numeroSillas('4') 

class vehiculo:
    def arrayCoches(
        Renault,
        Audi,
        Mercedes):
        print(arrayCoches)        

