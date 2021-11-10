#Principio SOLID de Abierto/Cerrado

class vehiculo:
    def _int_(self, precioMedio):
        self.precioMedio = precioMedio

class Renault:
    def get_precioMedio(self):
        return super().get_precioMedio('18000') 

class Audi:
    def get_precioMedio(self):
        return super().get_precioMedio('25000')

class Mercedes:
    def get_precioMedio(self):
        return super().get_precioMedio('27000')

class vehiculo:
    def arrayCoches(
        Renault,
        Audi,
        Mercedes):
        print(arrayCoches)
        


    
