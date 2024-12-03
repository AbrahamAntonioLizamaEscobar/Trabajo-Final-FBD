import flet as ft
from api import login_user, fetch_data, post_data

def main(page: ft.Page):
    page.title = "Sistema de Administración - Trabajo Final"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO

    def go_to_login(e):
        page.controls.clear()
        page.add(login_page())
        page.update()

    def go_to_admin(e):
        page.controls.clear()
        page.add(admin_dashboard())
        page.update()

    def go_to_bitacora(e):
        page.controls.clear()
        page.add(bitacora_screen())
        page.update()

    # Pantalla de Inicio
    def home_screen():
        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text("¡Bienvenido!", size=30, weight=ft.FontWeight.BOLD),
                ft.Text("Sistema de Administración", size=20),
                ft.ElevatedButton("Iniciar Sesión", on_click=go_to_login),
            ],
        )

    # Pantalla de Login
    def login_page():
        username = ft.TextField(label="Username", width=300)
        password = ft.TextField(label="Password", password=True, width=300)
        error_message = ft.Text("", color="red")

        def handle_login(e):
            response = login_user(username.value, password.value)
            if response["success"]:
                go_to_admin(e)
            else:
                error_message.value = "Credenciales incorrectas"
                error_message.update()

        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text("Iniciar Sesión", size=30, weight=ft.FontWeight.BOLD),
                username,
                password,
                error_message,
                ft.ElevatedButton("Ingresar", on_click=handle_login),
            ],
        )

    # Zona de Administración
    def admin_dashboard():
        return ft.Tabs(
            tabs=[
                ft.Tab(text="Usuarios", content=crud_table("usuarios")),
                ft.Tab(text="Roles", content=crud_table("roles")),
                ft.Tab(text="Proyectos", content=crud_table("proyectos")),
                ft.Tab(text="Gasolineras", content=crud_table("gasolineras")),
                ft.Tab(text="Vehículos", content=crud_table("vehiculos")),
            ]
        )

    # Pantalla Bitácora
    def bitacora_screen():
        usuario = ft.Dropdown(label="Usuario", options=get_dropdown_options("usuarios"))
        vehiculo = ft.Dropdown(label="Vehículo", options=get_dropdown_options("vehiculos"))
        gasolinera = ft.Dropdown(label="Gasolinera", options=get_dropdown_options("gasolineras"))
        km_inicial = ft.TextField(label="Kilómetros Iniciales")
        km_final = ft.TextField(label="Kilómetros Finales")
        num_galones = ft.TextField(label="Cantidad de Galones")
        costo = ft.TextField(label="Costo Total")
        tipo_gasolina = ft.TextField(label="Tipo de Gasolina")
        mensaje = ft.Text("")

        def guardar_bitacora(e):
            data = {
                "id_usr": usuario.value,
                "id_vehiculo": vehiculo.value,
                "id_gasolinera": gasolinera.value,
                "km_inicial": km_inicial.value,
                "km_final": km_final.value,
                "num_galones": num_galones.value,
                "costo": costo.value,
                "tipo_gasolina": tipo_gasolina.value,
            }
            response = post_data("bitacora", data)
            if response["success"]:
                mensaje.value = "¡Bitácora guardada exitosamente!"
            else:
                mensaje.value = "Error al guardar bitácora."
            mensaje.update()

        return ft.Column(
            controls=[
                ft.Text("Registro de Combustible", size=30, weight=ft.FontWeight.BOLD),
                usuario,
                vehiculo,
                gasolinera,
                km_inicial,
                km_final,
                num_galones,
                costo,
                tipo_gasolina,
                ft.ElevatedButton("Guardar", on_click=guardar_bitacora),
                mensaje,
            ]
        )

    # Componente CRUD genérico
    def crud_table(endpoint):
        data = fetch_data(endpoint)
        table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text(header)) for header in data[0].keys()
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(value)) for value in row.values()
                    ]
                ) for row in data
            ]
        )
        return ft.Column(controls=[table])

    # Cargar Dropdown (opciones)
    def get_dropdown_options(endpoint):
        data = fetch_data(endpoint)
        return [ft.dropdown.Option(value=row["id"], label=row["nombre"]) for row in data]

    page.add(home_screen())

ft.app(target=main)
