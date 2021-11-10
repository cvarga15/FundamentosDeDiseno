#Principio SOLID de Segregacion de Interfaz

class IAve:
    def comer(self):
        pass

class IAveVoladora:
    def volar(self):
        pass

class IAveNadadora:
    def nadar(self):
        pass    

class loro(IAve, IAveVoladora):
    def comer(self):
        pass

    def volar(self):
        pass

class pinguino(IAve, IAveNadadora):
    def comer(self):
        pass   
    def nadar(self):
        pass



