import flet as ft
def main(page: ft.Page):
    page.title="Sveika, pasaule!"
    teksts=ft.Text("=)")
    poga=ft.ElevatedButton(content="Nospied mani!")
    page.add(teksts, poga)

ft.run(main) 