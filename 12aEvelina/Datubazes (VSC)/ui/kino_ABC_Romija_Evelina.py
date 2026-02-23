import sqlite3
import flet as ft

savienojums = sqlite3.connect("kino_ABC_db_Romija_Evelina.db")
cursor = savienojums.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS filmas(
        filmas_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nosaukums TEXT NOT NULL,
        zanrs TEXT NOT NULL,
        ilgums TEXT NOT NULL,
        vecuma_ierobezojums INTEGER NOT NULL
)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS zales(
        zales_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nosaukums TEXT NOT NULL,
        vietu_skaits INTEGER NOT NULL
)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS seansi(
        seansi_id INTEGER PRIMARY KEY AUTOINCREMENT,
        zales_id INTEGER NOT NULL,
        filmas_id INTEGER NOT NULL,
        laiks TEXT NOT NULL,
        cena REAL NOT NULL,
        datums TEXT NOT NULL,
        FOREIGN KEY (filmas_id) REFERENCES filmas(filmas_id) ON DELETE CASCADE,
        FOREIGN KEY (zales_id) REFERENCES zales(zales_id) ON DELETE CASCADE
)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS biletes(
        biletes_id INTEGER PRIMARY KEY AUTOINCREMENT,
        seansi_id INTEGER NOT NULL,
        vards TEXT NOT NULL,
        FOREIGN KEY (seansi_id) REFERENCES seansi(seansi_id) ON DELETE CASCADE
)
""")

cursor.execute("SELECT COUNT(*)FROM filmas")
if cursor.fetchone()[0] == 0:
    filmas = [
        ("Frozen", "Multfilma", "1,5h",3),
        ("Zootopia", "Multfilma", "1,4h",5),
        ("Barbie", "Drāma", "2h",12),
        ("Avatars", "Fantastika", "3h",18),
        ("Bonds", "Trilleris", "1,5h",16),
        ("The Eras Tour: the Movie", "Koncertfilma", "3h", 13)
    ]
    cursor.executemany(
        "INSERT INTO filmas(nosaukums, zanrs, ilgums,vecuma_ierobezojums) VALUES (?, ?, ?,?)",
        filmas
    )

cursor.execute("SELECT COUNT(*)FROM zales")
if cursor.fetchone()[0] == 0:
    zales = [
        ("Alfa",100),
        ("Bravo", 50),
        ("Charlie",20),
        ("Delta",150),
        ("Echo",75)
    ]
    cursor.executemany(
        "INSERT INTO zales(nosaukums, vietu_skaits) VALUES (?, ?)",
        zales
    )

cursor.execute("SELECT COUNT(*)FROM seansi")
if cursor.fetchone()[0] == 0:
    seansi = [
        (1, 5, "16:00",10.9,"2026-09-09"),
        (2, 4, "18:00",20.8,"2026-10-09"),
        (3, 3, "23:00",12.8,"2026-08-09"),
        (4, 2, "21:00",10.8,"2026-05-09"),
        (5, 1, "12:00",14,"2026-03-09"),
        (6, 2, "22:00",13,"2026-03-08")
    ]
    cursor.executemany(
        "INSERT INTO seansi(filmas_id, zales_id, laiks,cena,datums) VALUES (?, ?, ?,?,?)",
        seansi
    )

cursor.execute("SELECT COUNT(*)FROM biletes")
if cursor.fetchone()[0] == 0:
    biletes = [
        (1,"Romija"),
        (2,"Evelīna"),
        (3,"Emma"),
        (4,"Valdis"),
        (5,"Atis"),
        (6,"Marta")
    ]
    cursor.executemany(
        "INSERT INTO biletes(seansi_id,vards) VALUES (?,?)",
        biletes
    )

savienojums.commit()

def main(page: ft.Page):
    page.title = "Bibliotēka"
    page.scroll=ft.ScrollMode.AUTO
    statuss = ft.Text("")

    def aizvert_dialogu(_):
        rezultatu_dialogs.open=False
        page.update()
    #piesiet "aizvērt" pogai funkciju
    
    def paradit_tabulu(virsraksts, kolonnas, rindas):
        #izveidot kolonnas
        datu_kolonnas = [] #nepieciešams kolonnām
        for k in kolonnas:
            kolonna=ft.DataColumn(ft.Text(k))
            datu_kolonnas.append(kolonna)

        datu_rindas=[]
        for rinda in rindas:
            cells=[] #šunai vienai rindai
            for vertiba in rinda:
                cell=ft.DataCell(ft.Text(vertiba))
                cells.append(cell)
            datu_rindas.append(ft.DataRow(cells=cells))
        
        #uztaisa tabulu
        tabula=ft.DataTable(
            columns=datu_kolonnas,
            rows=datu_rindas
        )

        #ieliek tabulu dialoglogā
        rezultatu_dialogs.title=ft.Text(virsraksts)
        rezultatu_dialogs.content=ft.Container(
            content=ft.Column(
                [
                    ft.Text(f"Rindu skaits: {len(rindas)}"),
                    ft.Divider(),
                    tabula
                ],
                    scroll=ft.ScrollMode.AUTO
            ),
            width=900,
            height=500
        )
        rezultatu_dialogs.open=True
        page.update()

    def izpildit_un_paradit(virsraksts,sql,kolonnas,ievietojamais=()):
        try:
            cursor.execute(sql, ievietojamais)
            rindas=cursor.fetchall()
            paradit_tabulu(virsraksts,kolonnas, rindas)
        except Exception as e:
            statuss.value=f"Kļūda vaicājumā: {e}"
            page.update()

    def vaicajums1(_):
        izpildit_un_paradit(
            "Rādīt visus seansus",
            """SELECT filmas.nosaukums, zales.nosaukums, seansi.datums, seansi.laiks, seansi.cena 
            FROM seansi 
            JOIN filmas ON filmas.filmas_id = seansi.filmas_id
            JOIN zales ON zales.zales_id = seansi.zales_id""",
            ["Filmas nosaukums","Zāles nosaukums","Datums","Laiks","Cena"]
        )

    poga_v1=ft.OutlinedButton("Visi seansi",on_click=vaicajums1)

    def ieladet_dropdownus():
        try:
            cursor.execute(
                """
                SELECT filmas_id, nosaukums
                FROM filmas
                ORDER BY nosaukums
                """
            )
            filmas = cursor.fetchall()
            filmas_izvele.options = [
                ft.dropdown.Option(key=str(r[0]), text=f"{r[1]}")
                for r in filmas
            ]

            #ja iepriekš bija izvēle, bet vairs nav options sarakstā
            if filmas_izvele.value not in [o.key for o in filmas_izvele.options]:
                filmas_izvele.value = None

        except Exception as e:
            statuss.value = f"Kļūda ielādējot dropdownus: {e}"

    def vaicajums2(_):
        izpildit_un_paradit(
            "Filmas seansi", 
            """SELECT filmas.nosaukums, zales.nosaukums, seansi.datums, seansi.laiks, seansi.cena
            FROM seansi
            JOIN filmas ON filmas.filmas_id = seansi.filmas_id
            JOIN zales ON zales.zales_id = seansi.zales_id
            WHERE filmas.filmas_id = ?
            ORDER BY filmas.nosaukums
            """,
            ["Filmas nosaukums", "Zāles nosaukums", "Datums", "Laiks", "Biļetes cena"],
            (filmas_izvele.value)
        )

    filmas_izvele = ft.Dropdown(label="Izvēlies filmu", width=150, on_select=vaicajums2)

    ieladet_dropdownus()

    def vaicajums3(_):
        izpildit_un_paradit(
            "Rādīt visus seansus",
            """SELECT filmas.nosaukums, zales.nosaukums, seansi.datums, seansi.laiks, seansi.cena 
            FROM seansi 
            JOIN filmas ON filmas.filmas_id = seansi.filmas_id
            JOIN zales ON zales.zales_id = seansi.zales_id
            ORDER BY seansi.datums, seansi.laiks ASC""",
            ["Filmas nosaukums","Zāles nosaukums","Datums","Laiks","Cena"]
        )
        page.update()

    def vaicajums4(_): 
        izpildit_un_paradit(
            "Klientu dati",
            """SELECT biletes.vards, filmas.nosaukums
            FROM seansi 
            JOIN filmas ON filmas.filmas_id = seansi.filmas_id
            JOIN biletes ON biletes.seansi_id = seansi.seansi_id
            ORDER BY vards""",
            ["Klienta vārds","Filmas nosaukums"]
        )

    def vaicajums5(_):
        izpildit_un_paradit(
            "Zāļu aizņemtība",
            """SELECT zales.nosaukums, COUNT(filmas.filmas_id)
            FROM seansi 
            JOIN filmas ON filmas.filmas_id = seansi.filmas_id
            JOIN zales ON zales.zales_id = seansi.zales_id
            GROUP BY zales.nosaukums""",
            ["Zāles nosaukums","Seansu skaits"]
        )

    rezultatu_dialogs = ft.AlertDialog(
        modal = True,
        title =ft.Text("Rezultāti"),
        content = ft.Text(""),
        actions = [
            ft.TextButton("Nekārtoti seansi", on_click=vaicajums1),
            ft.TextButton("Kārtot pēc laika", on_click=vaicajums3),
            ft.TextButton("Klientu dati", on_click=vaicajums4),
            ft.TextButton("Zāļu aizņemtība", on_click=vaicajums5),
            ft.TextButton("Aizvērt", on_click=aizvert_dialogu)
            ]
    )

    page.overlay.append(rezultatu_dialogs) #bez šī logs var neparādīties


    page.add(
        ft.Text("Vaicājumi"),
        ft.Row([poga_v1,filmas_izvele],wrap=True),
        ft.Divider(),
        statuss,
    )

    page.update()

ft.app(target=main)