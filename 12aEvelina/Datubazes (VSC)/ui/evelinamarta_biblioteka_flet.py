import flet as ft
import sqlite3

savienojums = sqlite3.connect("biblioteka_evelinamarta.db")
cursor = savienojums.cursor()

#-------------TABULU IZVEIDE--------------------------------------------------------------------------------------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS gramatas(
    gramatas_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nosaukums TEXT NOT NULL,
    autors TEXT NOT NULL,
    gads TEXT NOT NULL,
    zanrs TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS lasitaji(
    lasitaji_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT NOT NULL,
    uzvards TEXT NOT NULL,
    klase TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS iznemtas_gramatas(
    iznemtas_gramatas_id INTEGER PRIMARY KEY AUTOINCREMENT,
    gramatas_id INTEGER NOT NULL,
    lasitaji_id INTEGER NOT NULL,
    datums TEXT NOT NULL,
    atdots INTEGER NOT NULL,
    FOREIGN KEY (gramatas_id) REFERENCES gramatas(gramatas_id) ON DELETE CASCADE,
    FOREIGN KEY (lasitaji_id) REFERENCES lasitaji(lasitaji_id) ON DELETE CASCADE
)
""")

#---------------FLET LOGA IZVEIDE-------------------------------------------------------------------------------------------------------------------

def main(page:ft.Page):
    page.title="Bibliotēkas sistēma"

    #gramatas saglabasanas funkcijas izveide----------------------------------------------------------------------------------------------------------

    gramat_teksts = ft.Text("Jaunas grāmatas ievade!")
    
    nosaukums=ft.TextField(label="Nosaukums:")
    autors=ft.TextField(label="Autors:")
    gads=ft.TextField(label="Gads:")
    zanrs=ft.TextField(label="Žanrs:")

    statuss=ft.Text("")

    def saglabat_gramatu(_):
        lauks_nosaukums=nosaukums.value.strip()  
        lauks_autors=autors.value.strip()
        lauks_gads=gads.value.strip()
        lauks_zanrs=zanrs.value.strip()

        if "" in [lauks_nosaukums, lauks_autors, lauks_gads, lauks_zanrs]: #ja kaut kas ir tukss, nelauj pievienot datubazei
            statuss.value="Kļūda: aizpildi visus laukus!"
            statuss.color="red"
        elif not lauks_gads.isdigit():
            statuss.value="Kļūda: gads var būt tikai skaitlis!"
            statuss.color="red"
        else:
            cursor.execute("""
                INSERT INTO gramatas(nosaukums, autors, gads, zanrs)
                VALUES(?,?,?,?)
            """, (lauks_nosaukums, lauks_autors, lauks_gads, lauks_zanrs))
            savienojums.commit()
            page.update()
            statuss.value="Dati pievienoti!"
            statuss.color="green"

        nosaukums.value=""
        autors.value=""
        zanrs.value=""
        gads.value=""
        
        page.update()

    poga_gramatas=ft.ElevatedButton("Saglabāt datus", on_click=saglabat_gramatu)

    #lasitaja saglabasanas funkcijas izveide------------------------------------------------------------------------------------------------------------

    lasitaju_teksts=ft.Text("Jauna lasītāja ievade!")

    vards=ft.TextField(label="Vārds:")
    uzvards=ft.TextField(label="Uzvārds:")
    klase=ft.TextField(label="Klase:")

    def saglabat_lasitajus(_):
        lauks_vards=vards.value.strip()
        lauks_uzvards=uzvards.value.strip()
        lauks_klase=klase.value.strip()

        if "" in [lauks_vards, lauks_uzvards, lauks_klase]: #ja kaut kas ir tukss, nelauj pievienot datubazei
            statuss2.value="Kļūda: aizpildi visus laukus!"
            statuss2.color="red"
        else:
            cursor.execute("""
                INSERT INTO lasitaji(vards, uzvards, klase)
                VALUES(?,?,?)
            """, (lauks_vards, lauks_uzvards, lauks_klase))
            savienojums.commit()
            page.update()
            statuss2.value="Dati pievienoti!"
            statuss2.color="green"
        
        vards.value=""
        uzvards.value=""
        klase.value=""
        
        page.update()

    statuss2=ft.Text("")
    poga_lasitaji=ft.ElevatedButton("Saglabāt datus", on_click=saglabat_lasitajus)

    #iznemtu gramatu registracijas funkcija-------------------------------------------------------------------------------------------------------------

    iznemtasgramatas_teksts=ft.Text(value="Izņemtas grāmatas ievade!")
    
    dd_gramata=ft.Dropdown(label="Izvēlies grāmatu")
    dd_lasitajs=ft.Dropdown(label="Izvēlies lasītāju")
    datums=ft.TextField(label="Izņemšanas datums (GGGG-MM-DD):")
    cb_atdots=ft.Checkbox(label="Atdots?", value=False)

    def ieladet_dropdown():
        cursor.execute("""
        SELECT * FROM gramatas
        ORDER BY nosaukums
        """)
        gramatas=cursor.fetchall()
        for r in gramatas:
            dd_gramata.options.append(ft.dropdown.Option(key=str(r[0]),text=f"{r[1]}, ({r[2]}, {r[3]})")) 
        
        cursor.execute("""
        SELECT * FROM lasitaji
        ORDER BY uzvards, vards
        """)
        lasitaji=cursor.fetchall()
        for r in lasitaji:
            dd_lasitajs.options.append(ft.dropdown.Option(key=str(r[0]), text=f"{r[1]} {r[2]}, {r[3]}"))
        
        page.update()

    ieladet_dropdown()

    def saglabat_iznemtu(_):
        if dd_gramata.value is None or dd_lasitajs.value is None or datums.value=="": #ja kaut kas ir tukss, nelauj pievienot datubazei
            statuss3.value="Kļūda! Aizpildi visus laukus!"
            statuss3.color="red"
        else:
            gramatas_id = dd_gramata.value.strip()
            lasitaji_id = dd_lasitajs.value.strip()
            datums_db = datums.value.strip()
            atdots_vertiba = cb_atdots.value
            ievietot = 0

            if atdots_vertiba == True:
                ievietot = 1
            elif atdots_vertiba == False:      #parveido checkbox bool uz 0/1 int ievietosanai datubaze
                ievietot = 0

            cursor.execute("""
            INSERT INTO iznemtas_gramatas(gramatas_id, lasitaji_id, datums, atdots)
            VALUES(?,?,?,?)
            """,
            (int(gramatas_id), int(lasitaji_id), datums_db, int(ievietot)))
            
            savienojums.commit()
            statuss3.value="Dati pievienoti!"
            statuss3.color="green"

            dd_gramata.value=""
            dd_lasitajs.value=""
            datums.value=""

            page.update()

    poga_iznemta=ft.ElevatedButton("Saglabāt datus", on_click=saglabat_iznemtu)
    statuss3=ft.Text(value="")

    #visu detalu pievienosana logam---------------------------------------------------------------------------------------------------------------------

    page.add(
        gramat_teksts,
        nosaukums,autors,gads,zanrs,
        statuss,
        poga_gramatas,

        lasitaju_teksts,
        vards,uzvards,klase,
        statuss2,
        poga_lasitaji,
        
        iznemtasgramatas_teksts,
        dd_gramata,dd_lasitajs,datums,cb_atdots,
        statuss3,
        poga_iznemta
    )    

ft.run(main)