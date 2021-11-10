#Principio SOLID de Inversion de Dependencias

class DatabaseService():
    def _init_(self, conexion):
        self.conexion = conexion
    def dato(self):
        self.getDatos = getDatos
        self.setDatos = setDatos

class APIService():
    def _init_(self, conexion):
        self.conexion = conexion
    def dato(self):
        self.getDatos = getDatos
        self.setDatos = setDatos      

