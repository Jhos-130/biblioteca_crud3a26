from database.conexion import Conexion
from models.carrera import Carrera

class CarreraDAO:
    
    def obtener_todos(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        
        cursor.execute("SELECT * FROM carrera")
        registros = cursor.fetchall()
        
        carreras = []
        for registro in registros:
            carrera = Carrera(registro[0], registro[1])
            carreras.append(carrera)
            
        cursor.close()
        conexion.close()
        return carreras