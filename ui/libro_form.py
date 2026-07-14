import flet as ft

def libro_form():
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
        else:
            mensaje.value = f"Libro '(titulo)' listo para insertar"
            print(f"Titulo: '(titulo)', Autor: '(autor)', ISBN: '(isbn)'")
            mensaje.color = ft.Colors.GREEN
            titulo_input.value = ""
            autor_input.value = ""
            isbn_input.value = ""

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
                
                ft.ElevatedButton(
                    "Refistrar libro",
                    icon = ft.Icons.SAVE,
                    on_click = guardar_libro
                ),

                mensaje

            ],
            spacing = 15
        )
    )