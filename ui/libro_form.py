import flet as ft

from dao.libro_dao import LibroDAO
from models.libro import Libro

def libro_form(regresar):
    titulo_input = ft.TextField(
        label="Titulo del libro: ",
        width = 400
    )

    autor_input = ft.TextField(
        label="Autor del libro: ",
        width = 400
    )

    isbn_input = ft.TextField(
        label="ISBN: ",
        width = 400
    )

    mensaje = ft.Text(
        "",
        color = ft.Colors.GREEN
    )

    def guardar_libro(e):
        #Recupera los valores de los TextField
        titulo = titulo_input.value
        autor = autor_input.value
        isbn = isbn_input.value

        if titulo == "" or autor == "" or isbn == "":
            mensaje.value = "   Todos los campos son obligatorios"
            mensaje.color = ft.Colors.RED
            e.page.update()
            return
        
        try:
            libro_dao = LibroDAO()
            id = libro_dao.obtener_ultimo_id() + 1

            nuevo_libro = Libro(
                id = id,
                titulo = titulo,
                autor = int(autor),
                isbn = isbn,
                disponible = True
            )

            libro_dao.insertar(nuevo_libro)


            mensaje.value = f"Libro '{titulo}' ha sido insertado"
            mensaje.color = ft.Colors.GREEN
            titulo_input.value = ""
            autor_input.value = ""
            isbn_input.value = ""

        except ValueError:
            mensaje.value = "El campo 'Autor' debe ser un numero entero"
            mensaje.color = ft.Colors.RED
        except Exception as error:
            mensaje.value = f"Error al insertar libro: {error}"
            mensaje.color = ft.Colors.RED


        e.page.update()

    return ft.Container(
        padding = 30,
        content = ft.Column(
            controls = [
                ft.Text(
                    "Registrar nuevo libro",
                    size = 24,
                    weight = ft.FontWeight.BOLD
                ),
                
                ft.Text(
                    "Captura los datos básicos del libro",
                    size = 14,
                    color = ft.Colors.BLUE_GREY_600
                ),

                titulo_input,
                autor_input,
                isbn_input,
                
                ft.Row(
                    controls = [
                        ft.ElevatedButton(
                            "Refistrar libro",
                            icon = ft.Icons.SAVE,
                            on_click = guardar_libro
                        ),
                        ft.OutlinedButton(
                            "Regresar",
                            icon = ft.Icons.ARROW_BACK,
                            on_click = lambda e: regresar()
                        )
                    ]
                ),

                mensaje

            ],
            spacing = 15
        )
    )