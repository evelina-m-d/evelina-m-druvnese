import flet as ft
def main(page: ft.Page):
    page.title="Sveika, pasaule!"
    teksts=ft.Text("Nospied pogu!")
    def poga_nospiesta(_):
        teksts.value="Poga nospiesta!"
        page.update()
    poga=ft.ElevatedButton(content="Nospied mani!", on_click=poga_nospiesta)
    page.add(teksts, poga)

ft.run(main)