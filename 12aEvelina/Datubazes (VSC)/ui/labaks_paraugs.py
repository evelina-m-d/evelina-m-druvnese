import flet as ft

def main(page:ft.Page):
    page.title=":3"
    virsraksts=ft.Text(
        value=":P",
        size=27,
        weight=ft.FontWeight.BOLD,
        color="pink"
    )

    vards=ft.TextField(
        label="Ievadi vārdu:",
        width=200
    )

    uzvards=ft.TextField(
        label="Ievadi uzvārdu:",
        width=200
    )

    rezultats=ft.Text(value="Sveikii!",size=20,color="pink")

    dialogs=ft.AlertDialog(
        title=ft.Text("Haii :>"),
        content=ft.Text("Ka tev iet??"),
        actions=[
            ft.TextButton("aizvērt :(", on_click=lambda e:page.close(dialogs))
        ]
        )
        
    

    def paradit_sveicienu(_):
        if vards.value.strip()=="" or uzvards.value.strip()=="":
            rezultats.value="Lūdzu, aizpildi abus lauciņus :<"
            rezultats.color="purple"
        else:
            rezultats.value=f"Sveiki, {vards.value} {uzvards.value}! Būsi mans draugs? ^-^"
            rezultats.color="purple"
        page.update()

    poga_sveiciens=ft.ElevatedButton(
        content="Sasveicinies!",
        on_click=paradit_sveicienu
    )

    def atvert_logu(_):
        page.open(dialogs)

    poga_logs = ft.OutlinedButton(
        content= "Nospied mani!",
        on_click=atvert_logu
    )

    page.add(virsraksts,vards,uzvards,poga_sveiciens,poga_logs,rezultats)


ft.run(main)