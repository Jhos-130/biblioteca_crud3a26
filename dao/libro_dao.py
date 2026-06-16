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
        registros = cursor.fetchall

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
    
    def insertar(self, libro): 
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        sql = """
        INSERT INTO libro (titulo, autor, isbn, disponible)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(
            sql,
            (libro.titulo,
             libro.autor,
             libro.isbn,
             libro.disponible)
        )

        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self, libro):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE libro
        SET titulo = %s, autor = %s, isbn = %s,
        disponible = %s
        WHERE id = %s
        """

        cursor.execute(
            sql,
            (libro.titulo,
             libro.autor,
             libro.isbn,
             libro.disponible,
             libro.id)
        )
        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self, libro_id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            " DELETE FROM libro WHERE id = %s",
            (libro_id,)
            )
        conexion.commit()
        cursor.close()
        conexion.close()