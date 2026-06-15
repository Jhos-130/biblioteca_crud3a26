#DAO:Data Access Object
#libro_dao: Objeto de acceso a datos de la tabla

from database.conexion import Conexion
from models.libro import Libro

class LibroDAO:

     # SELECT * FROM libro
    def obtener_todos(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM libro")
        registros = cursor.fetchall()

        libros = []
        for registro in registros:
            libro = Libro(
            registro.id, 
            registro.titulo,
            registro.autor,
            registro.isbn,
            registro.disponible)
            libros.append(libro)
        cursor.close()
        conexion.close()
        return libros