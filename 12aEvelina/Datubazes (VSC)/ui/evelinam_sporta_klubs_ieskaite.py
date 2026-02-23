#sporta_centrs_skelets_vienkars.py
#skolēnam jāieliek SQL vaicājumi, pogas, jāizvieto elementi lapā(page.add)

import flet as ft
import sqlite3

def main(page: ft.Page):
    page.title = "Sporta centrs 'LACE'"
    page.scroll=ft.ScrollMode.AUTO
    page.window_width = 1000
    page.window_height = 700

    #Savienojums ar DB (DB fails tajā pašā mapē)
    savienojums = sqlite3.connect("sporta_centrs_datubaze.db", check_same_thread=False)
    cursor = savienojums.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    #Flet elementi
    virsraksts = ft.Text("Sporta centrs – vaicājumi", size=22, weight=ft.FontWeight.BOLD)
    statuss = ft.Text("")

    #Dropdown(trenera izvēlei)
    treneri_dropdown = ft.Dropdown(
        label="Izvēlies treneri (filtram)",
        width=320,
        options=[]
    )

    #rezultātu tabula
    tabula = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nodarbība")),
            ft.DataColumn(ft.Text("Treneris")),
            ft.DataColumn(ft.Text("Zāle")),
            ft.DataColumn(ft.Text("Datums")),
            ft.DataColumn(ft.Text("Laiks")),
            ft.DataColumn(ft.Text("Cena")),
        ],
        rows=[]
    )

    #funkcija, kas ieliek datus tabulā
    def paradit_tabula(kolonnas, rindas):
        #iestata kolonnas
        tabula.columns = []
        for k in kolonnas:
            tabula.columns.append(ft.DataColumn(ft.Text(k)))

        tabula.rows = [] #Notīra vecās rindas

        #Ja nav datu, parāda paziņojumu
        if len(rindas) == 0:
            statuss.value = "Nav atrasti dati."
            page.update()
            return

        statuss.value = ""

        #Ieliek rindas tabulā
        for rinda in rindas:
            cells = []
            for vertiba in rinda:
                cells.append(ft.DataCell(ft.Text(str(vertiba))))
            tabula.rows.append(ft.DataRow(cells=cells))

        page.update()#neaizmirsti atjaunot lapu

    #dropdown aizpildīšana no datubazes, panemot treneru vardus
    cursor.execute("SELECT vards FROM treneri ORDER BY vards;")
    treneri = cursor.fetchall()  
    treneri_dropdown.options = [ft.dropdown.Option(t[0]) for t in treneri]

    def poga_visas_nodarbibas(_):
        #vaic1-Rādīt visas nodarbības
        sql = """
        SELECT
            nodarbibas.nosaukums, 
            concat(treneri.vards, " ", treneri.uzvards),
            zales.nosaukums,
            nodarbibas.datums,
            nodarbibas.sakuma_laiks,
            nodarbibas.cena
        FROM nodarbibas
        JOIN treneri ON treneri.trenera_id = nodarbibas.trenera_id
        JOIN zales ON zales.zales_id = nodarbibas.zales_id
        """
        cursor.execute(sql)
        rindas = []
        rindas = cursor.fetchall()

        kolonnas = ["Nodarbība", "Treneris", "Zāle", "Datums", "Laiks", "Cena"]
        paradit_tabula(kolonnas, rindas)

    def poga_filtret_pec_trenera(_):
        #vaic2-Filtrēt pēc trenera (Dropdown)
        izvelets_treneris = treneri_dropdown.value
        if izvelets_treneris is None:
            statuss.value = "Izvēlies treneri no Dropdown!"
            statuss.color = "TEAL"
            page.update()
            return

        sql = """
        SELECT
            nodarbibas.nosaukums, 
            concat(treneri.vards, " ", treneri.uzvards),
            zales.nosaukums,
            nodarbibas.datums,
            nodarbibas.sakuma_laiks,
            nodarbibas.cena
        FROM nodarbibas
        JOIN treneri ON treneri.trenera_id = nodarbibas.trenera_id
        JOIN zales ON zales.zales_id = nodarbibas.zales_id
        WHERE treneri.vards = ?
        """
        cursor.execute(sql, (izvelets_treneris,))
        rindas = []
        rindas = cursor.fetchall()

        kolonnas = ["Nodarbība", "Treneris", "Zāle", "Datums", "Laiks", "Cena"]
        paradit_tabula(kolonnas, rindas)
    
    def poga_zales(_):
        #vaic3-Rādīt zāles
        sql = """
        SELECT
            nosaukums, vietu_skaits
        FROM zales
        """
        cursor.execute(sql)
        rindas = []
        rindas = cursor.fetchall()

        kolonnas = ["Zāle", "Vietu skaits"]
        paradit_tabula(kolonnas, rindas)

    def poga_treneri(_):
        #vaic4-Rādīt trenerus
        sql = """
        SELECT
            vards, uzvards, specializacija
        FROM treneri
        """
        cursor.execute(sql)
        rindas = []
        rindas = cursor.fetchall()

        kolonnas = ["Vārds", "Uzvārds", "Specializācija"]
        paradit_tabula(kolonnas, rindas)

    def poga_apmeklejumi(_):
        #vaic5-Rādīt apmeklējumus(JOIN)
        sql = """
        SELECT 
            apmeklejuma_id, nodarbibas.nosaukums, apmeklejuma_datums
        FROM apmeklejumi
        JOIN nodarbibas ON nodarbibas.nodarbibas_id = apmeklejumi.nodarbibas_id
        """
        cursor.execute(sql)
        rindas = []
        rindas = cursor.fetchall()

        kolonnas = ["Apmeklējums ID", "Nodarbība", "Datums"]
        paradit_tabula(kolonnas, rindas)

    def poga_skaits(_):
        #vaic5-Apmeklējumu skaits(COUNT + GROUP BY)
        sql = """
        SELECT nodarbibas.nosaukums, COUNT(apmeklejumi.apmeklejuma_id)
        FROM apmeklejumi
        JOIN nodarbibas ON nodarbibas.nodarbibas_id = apmeklejumi.nodarbibas_id
        GROUP BY nodarbibas.nosaukums
        """
        cursor.execute(sql)
        rindas = []
        rindas = cursor.fetchall()

        kolonnas = ["Nodarbība", "Apmeklējumu skaits"]
        paradit_tabula(kolonnas, rindas)

    #Pogas
    poga1 = ft.Button("Rādīt visas nodarbības", on_click=poga_visas_nodarbibas, style=ft.ButtonStyle(color={ft.ControlState.DEFAULT: ft.Colors.PINK_700}, bgcolor={ft.ControlState.HOVERED: ft.Colors.PINK_200}))
    poga2 = ft.Button("Filtrēt pēc trenera", on_click=poga_filtret_pec_trenera, style=ft.ButtonStyle(color={ft.ControlState.DEFAULT: ft.Colors.PINK_700}, bgcolor={ft.ControlState.HOVERED: ft.Colors.PINK_200}))
    poga3 = ft.Button("Rādīt zāles", on_click=poga_zales, style=ft.ButtonStyle(color={ft.ControlState.DEFAULT: ft.Colors.PINK_700}, bgcolor={ft.ControlState.HOVERED: ft.Colors.PINK_200}))
    poga4 = ft.Button("Rādīt trenerus", on_click=poga_treneri, style=ft.ButtonStyle(color={ft.ControlState.DEFAULT: ft.Colors.PINK_700}, bgcolor={ft.ControlState.HOVERED: ft.Colors.PINK_200}))
    poga5 = ft.Button("Rādīt apmeklējumus", on_click=poga_apmeklejumi, style=ft.ButtonStyle(color={ft.ControlState.DEFAULT: ft.Colors.PINK_700}, bgcolor={ft.ControlState.HOVERED: ft.Colors.PINK_200}))
    poga6 = ft.Button("Apmeklējumu skaits", on_click=poga_skaits, style=ft.ButtonStyle(color={ft.ControlState.DEFAULT: ft.Colors.PINK_700}, bgcolor={ft.ControlState.HOVERED: ft.Colors.PINK_200}))

    #Lapas izkārtojums
    page.add(
    treneri_dropdown,
    poga1,
    poga2,
    poga3,
    poga4,
    poga5,
    poga6,

    statuss,
    tabula
    )

ft.app(target=main)
