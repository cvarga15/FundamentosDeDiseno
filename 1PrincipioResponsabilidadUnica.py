#Principio SOLID de Responsabilidad Unica

class vehiculo(object): #Objeto vehiculo
    def _init_(self, marca): #atributo marca
        self.marca = marca

    def getmarca(self): #Metodo
        return self._marca() 

class vehiculoBBDD(object): #Objeto base de datos vehiculos
    def __init__(self, vehiculo, bd):       
        self._bd = bd
        self.vehiculo = vehiculo

class vehiculoPrinter(object): #Objeto imprimir vehiculo
    def __init__(self, vehiculo, bd): 
        self._bd = bd
        self.vehiculo = vehiculo

    def imprimir(self): #atributo imprimir
        return imprimir (self._vehiculo.getmarca())  