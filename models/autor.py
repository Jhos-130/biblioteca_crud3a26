class Autor:
    
    
    def __init__( self, id, nombre):
       self.id = id
       self.nombre = nombre

    def mostrar_info(self):
        return f"Autor ID: {self.id}, Nombre: {self.nombre}" 
