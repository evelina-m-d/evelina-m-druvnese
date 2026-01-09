import flet as ft
import sqlite3

def main(page: ft.Page):
    page.title="Šovu sistēma"

    #savienojums ar datubāzi
    savienojums = sqlite3.connect("testa_dati_tv_sovi.db")
    cursor = savienojums.cursor()

    sovu_teksts=ft.Text("Jauna šova ievade!")

    nosaukums=ft.TextField(label="Nosaukums:")
    kanals=ft.TextField(label="Kanāls:")
    zanrs=ft.TextField(label="Žanrs:")
    gads=ft.TextField(label="Gads:")

    def saglabat_tvsovus(_):
        lauks_nosaukums=nosaukums.value.strip()
        lauks_kanals=kanals.value.strip()
        lauks_zanrs=zanrs.value.strip()
        lauks_gads=gads.value.strip()

        if "" in [lauks_nosaukums, lauks_kanals, lauks_zanrs, lauks_gads]:
            statuss.value="Kļūda: aizpildi visus laukus!"
            statuss.color="red"
        else:
            cursor.execute("""
                INSERT INTO televizijas_sovi(nosaukums, kanals, zanrs, gads)
                VALUES(?,?,?,?)
            """, (lauks_nosaukums, lauks_kanals, lauks_zanrs, lauks_gads))
            savienojums.commit()
            statuss.value="Dati pievienoti!"
            statuss.color="green"

        nosaukums.value=""
        kanals.value=""
        zanrs.value=""
        gads.value=""
        
        page.update()

    poga_tvsovi=ft.ElevatedButton("Saglabāt datus", on_click=saglabat_tvsovus)

    #teksts statusam (vai visi dati ievaditi)
    statuss=ft.Text("")

    dalibnieku_teksts=ft.Text("Jauna dalībnieka ievade!")

    vards=ft.TextField(label="Vārds:")
    uzvards=ft.TextField(label="Uzvārds:")
    profesija=ft.TextField(label="Profesija:")

    def saglabat_dalibniekus(_):
        lauks_vards=vards.value.strip()
        lauks_uzvards=uzvards.value.strip()
        lauks_profesija=profesija.value.strip()

        if "" in [lauks_vards, lauks_uzvards, lauks_profesija]:
            statuss2.value="Kļūda: aizpildi visus laukus!"
            statuss2.color="red"
        else:
            cursor.execute("""
                INSERT INTO sovu_dalibnieki(vards, uzvards, profesija)
                VALUES(?,?,?)
            """, (lauks_vards, lauks_uzvards, lauks_profesija))
            savienojums.commit()
            statuss2.value="Dati pievienoti!"
            statuss2.color="green"
        
        vards.value=""
        uzvards.value=""
        profesija.value=""
        
        page.update()

    statuss2=ft.Text("")
    poga_dalibnieki=ft.ElevatedButton("Saglabāt datus", on_click=saglabat_dalibniekus)

    dalibu_teksts=ft.Text(value="Jaunas dalības ievade!")
    
    dd_dalibnieks=ft.Dropdown(label="Izvēlies dalībnieku")
    dd_sovs=ft.Dropdown(label="Izvēlies šovu")
    dd_loma=ft.TextField(label="Loma:")

    def ieladet_dropdown():
        cursor.execute("""
        SELECT * FROM sovu_dalibnieki
        ORDER BY uzvards, vards
        """)
        dal=cursor.fetchall()
        for r in dal:
            dd_dalibnieks.options.append(ft.dropdown.Option(key=str(r[0]),text=f"{r[1]} {r[2]}, {r[3]}"))
        
        cursor.execute("""
        SELECT * FROM televizijas_sovi
        ORDER BY nosaukums
        """)
        sovi=cursor.fetchall()
        dd_sovs.options=[
            ft.dropdown.Option(
                key=str(r[0]),
                text=f"{r[1]}, {r[2]}, {r[4]}"
            )
            for r in sovi
        ]
        page.update()

    ieladet_dropdown()

    def saglabat_dalibu(_):
        if dd_dalibnieks.value is None or dd_sovs.value is None or dd_sovs.value=="":
            statuss3.value="Kļuda! Aizpildi visus laukus!"
            statuss3.color="red"
        else:
            dal_id = dd_dalibnieks.value.strip()
            dal_sovs = dd_sovs.value.strip()
            dal_loma = dd_sovs.value.strip()

            cursor.execute("""
            INSERT INTO sovu_dalibas(sovu_dalibnieki_id, televizijas_sovi_id, loma)
            VALUES(?,?,?)
            """,
            (int(dal_id), int(dal_sovs), dal_loma)
            )
            savienojums.commit()
            statuss3.value="Dati pievienoti!"
            statuss3.color="green"

            dd_dalibnieks.value=""
            dd_sovs.value=""
            dd_loma.value=""

    poga_dalibas=ft.ElevatedButton("Saglabāt datus", on_click=saglabat_dalibu)
    statuss3=ft.Text(value="")

    page.add(
        sovu_teksts,
        nosaukums, 
        kanals, 
        zanrs, 
        gads, 
        statuss,
        poga_tvsovi,

        dalibnieku_teksts,
        vards,
        uzvards,
        profesija,
        statuss2,
        poga_dalibnieki,
        
        dalibu_teksts,
        dd_dalibnieks,
        dd_sovs,
        dd_loma,
        statuss3,
        poga_dalibas)

ft.run(main)