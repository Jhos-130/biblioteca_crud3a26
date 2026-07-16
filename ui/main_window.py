import flet as ft

from ui.libro_form import libro_form

def main_window(page: ft.Page):
    page.title = "Sistema de Biblioteca Universitaria"
    page.window_width = 1100
    page.window_heigt = 700
    page.padding = 0
    page.bgcolor = ft.Colors.BLUE_GREY_50

    titulo = ft.Text(
        "Sistema de Biblioteca Universitaria", 
          size=24,
          weight=ft.FontWeight.BOLD
    )

    subtitulo = ft.Text(
        "Selecciona una opción del menú",
        size = 16,
        color = ft.Colors.BLUE_GREY_600
    )

    # Widget Container
    contenido = ft.Container(
        padding = 30,
        expand = True,
        bgcolor = ft.Colors.WHITE
    )

    def inicio():
        return ft.Column(
            controls = [
                titulo,
                subtitulo
            ],
            spacing = 10
        )
    
    def mostrar_inicio(e=None):
        contenido.content = inicio()
        page.update()

    #Reacciona al click del boton de libros en el menu lateral
    def mostrar_insertar_libros(e):
        contenido.content = libro_form(mostrar_inicio)
        page.update()

    menu_lateral = ft.Container (
        width = 220,
        bgcolor = ft.Colors.BLUE_GREY_900,
        padding = 20,
        content = ft.Column(
            controls = [
                ft.Text(
                    "Biblioteca",
                    size = 22,
                    weight = ft.FontWeight.BOLD,
                    color = ft.Colors.WHITE
                ),
                ft.Text(
                    "Sistema de gestión",
                    size = 12,
                    color = ft.Colors.BLUE_GREY_100,
                ),
                ft.Divider(color = ft.Colors.BLUE_GREY_700),
                ft.ElevatedButton(
                    "Inicio",
                    icon = ft.Icons.HOME,
                    width = 180,
                    on_click = mostrar_inicio
                ),
                ft.ElevatedButton(
                    "Libros",
                    icon = ft.Icons.BOOK,
                    width = 180,
                    on_click = mostrar_insertar_libros
                ),
                ft.ElevatedButton(
                    "Usuarios",
                    icon = ft.Icons.BOOK,
                    width = 180,
                ),
                ft.ElevatedButton(
                    "Prestamos",
                    icon = ft.Icons.SWAP_HORIZ,
                    width = 180,
                ),
                ft.ElevatedButton(
                    "Devoluciones",
                    icon = ft.Icons.KEYBOARD_RETURN,
                    width = 180,
                ),
            ],
            spacing = 15
        )
    )
    

    layout = ft.Row(
        controls = [
            menu_lateral,
            contenido
        ],
        expand = True
    )

    page.add(layout)

    mostrar_inicio()