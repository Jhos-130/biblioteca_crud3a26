import flet as ft

from ui.main_window import main_window
from dao.libro_dao import LibroDAO
from models.libro import Libro
from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario

def ver_libros():
    try:
        libro_dao = LibroDAO()

        libros = libro_dao.obtener_todos()

        print("=== Libros en la biblioteca ===")

        if len(libros) == 0:
                print("No hay libros registrados.")
        else:
            for libro in libros:
                print("-------------------------------")
                print(
                    f"ID: {libro.id}, Titulo: {libro.titulo},\n"
                    f"Autor: {libro.autor}, ISBN: {libro.isbn},\n "
                    f"Disponible: {'Si' if libro.disponible else 'No'}"
                )
        print("-------------------------------")
        print("\n Conexion exitosa a la base de datos")
    except Exception as e:
        print("Error: ")
        print(e)

def insertar_libro():
    titulo = input("Escribe el titulo de un nuevo libro: ")
    autor = int(input("Escribe el id del autor: "))
    isbn = input("Escriba el isbn del nuevo libro: ")
    disponible = True
    try:
        libro_dao = LibroDAO()
        id = libro_dao.obtener_ultimo_id() + 1
        libro = Libro(id, titulo, autor, isbn, disponible)
        print("Insercion realizada con exito")
    except Exception as e:
        print("Error al insertar un nuevo libro")
        print(e)
    
def actualizar_libro():
    print("Selecciona el libro a actualizar ")
    try:
        libro_dao = LibroDAO()
        ver_libros()
        id = int(input("Escribe el id del libro a actualizar: "))
        titulo = input("Escribe el nuevo titulo: ")
        autor = int(input("Escribe el nuevo autor: "))
        isbn = input("Escribe el nuevo ISBN: ")
        disponible = bool(input("Escribe el nuevo valor de disponible: "))
        libro = Libro(id, titulo, autor, isbn, disponible)
        libro_dao.actualizar(libro)
        print(f"El libro {id} se ha actualizado exitosamente")

    except Exception as e:
        print("Error al insertar un libro")
        print(e)

def eliminar_libro():
    try:
        libro_dao = LibroDAO()
        print("Lista de libros disponibles:")
        ver_libros()
        id = int(input("Escribe el id del libro a eliminar: "))
        libro_dao.eliminar(id)
        print(f"El libro {id} ha sido eliminado con éxito")
    except Exception as e:
        print(f"Error al eliminar el libro {id}")
        print(e)

def ver_usuarios():
    try:
        usuario_dao = UsuarioDAO()
        usuarios = usuario_dao.obtener_todos()
        
        print("\n=== Usuarios en la biblioteca ===")
        if len(usuarios) == 0:
            print("No hay usuarios registrados.")
        else:
            for usuario in usuarios:
                print("-" * 40)
                print(
                    f"ID: {usuario.id_usuario}, Nombre: {usuario.nombre}\n"
                    f"Email: {usuario.email}, Carrera: {usuario.carrera}"
                )
            print("-" * 40)
        print("\nConexion exitosa a la base de datos")
    except Exception as e:
        print(f"Error: {e}")

def insertar_usuario():
    nombre = input("Escribe el nombre del nuevo usuario: ")
    email = input("Escribe el email del nuevo usuario: ")
    matricula = input("Escribe la matrícula del nuevo usuario: ")
    carrera = input("Escribe el nombre de la carrera: ")
    try:
        usuario_dao = UsuarioDAO()
        id_usuario = usuario_dao.obtener_ultimo_id() + 1
        usuario = Usuario(id_usuario, nombre, matricula, email, carrera)
        usuario_dao.insertar(usuario)
        print("Insercion realizada con exito")
    except Exception as e:
        print("Error al insertar un nuevo usuario")
        print(e)

def actualizar_usuario():
    print("Selecciona el usuario a actualizar")
    try:
        usuario_dao = UsuarioDAO()
        ver_usuarios()
        id_usuario = int(input("Escribe el id del usuario a actualizar: "))
        nombre = input("Escribe el nuevo nombre: ")
        matricula = input("Escribe la matrícula del nuevo usuario: ")
        email = input("Escribe el nuevo email: ")
        carrera = input("Escribe la nueva carrera: ")
        usuario = Usuario(id_usuario, nombre, matricula, carrera, email)
        usuario_dao.actualizar(usuario)
        print(f"El usuario {id_usuario} se ha actualizado exitosamente")
    except Exception as e:
        print("Error al actualizar el usuario")
        print(e)

def eliminar_usuario():
    try:
        usuario_dao = UsuarioDAO()
        print("Lista de usuarios disponibles:")
        ver_usuarios()
        id_usuario = int(input("Escribe el id del usuario a eliminar: "))
        usuario_dao.eliminar(id_usuario)
        print(f"El usuario {id_usuario} ha sido eliminado con exito")
    except Exception as e:
        print(f"Error al eliminar el usuario")
        print(e)

ft.app(target = main_window)

# def main():
#     print("=== BIBLIOTECA UNIVERSITARIA ===")
#     print("Menu de opciones")
#     print("1. Ver todos los libros")
#     print("2. Insertar un nuevo libro")
#     print("3. Actualizar un libro disponible")
#     print("4. Eliminar u libro disponible")
#     print("5. Ver todos los usuarios")       
#     print("6. Insertar un nuevo usuario")    
#     print("7. Actualizar un usuario")         
#     print("8. Eliminar un usuario")           
#     opcion = int(input("Selecciona una opcion (1-8): "))

#     match opcion:
#         case 1:
#             ver_libros()
#         case 2:
#             insertar_libro()
#         case 3:
#             actualizar_libro()
#         case 4:
#             eliminar_libro()
#         case 5:
#             ver_usuarios()
#         case 6:
#             insertar_usuario()  
#         case 7:
#             actualizar_usuario()  
#         case 8:
#             eliminar_usuario()
    

# if __name__ == "__main__":
#     main()


