# DAO: Data Access Object
# usuario_dao: Objeto de acceso a datos de la tabla usuario

from database.conexion import Conexion
from models.usuario import Usuario

class UsuarioDAO:

    def obtener_todos(self):
        conexion = Conexion.obtain_conexion() if hasattr(Conexion, 'obtain_conexion') else Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, matricula, correo, carrera FROM usuario")
        registros = cursor.fetchall()
        
        usuarios = []
        for registro in registros:
            usuario = Usuario(
                id_usuario=registro[0],
                nombre=registro[1],
                matricula="",
                email=registro[2],
                carrera=registro[3]
            )
            usuarios.append(usuario)
            
        cursor.close()
        conexion.close()
        return usuarios

    def insertar(self, usuario):
        conexion = Conexion.obtain_conexion() if hasattr(Conexion, 'obtain_conexion') else Conexion.obtener_conexion()
        cursor = conexion.cursor()
        sql = """
        INSERT INTO usuario (id, nombre, matricula, carrera, correo)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (usuario.id_usuario, usuario.nombre, usuario.matricula, usuario.carrera, usuario.email))
        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self, usuario):
        conexion = Conexion.obtain_conexion() if hasattr(Conexion, 'obtain_conexion') else Conexion.obtener_conexion()
        cursor = conexion.cursor()
        sql = """
        UPDATE usuario
        SET nombre = %s, matricula = %s, carrera = %s, correo = %s
        WHERE id = %s
        """
        cursor.execute(sql, (usuario.nombre, usuario.matricula, usuario.email, usuario.carrera, usuario.id_usuario))
        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self, usuario_id):
        conexion = Conexion.obtain_conexion() if hasattr(Conexion, 'obtain_conexion') else Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM usuario WHERE id = %s", (usuario_id,))
        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_ultimo_id(self):
        conexion = Conexion.obtain_conexion() if hasattr(Conexion, 'obtain_conexion') else Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id FROM usuario ORDER BY id DESC")
        resultado = cursor.fetchone()
        
        cursor.close()
        conexion.close()
        
        if resultado is None:
            return 0
        return resultado[0]