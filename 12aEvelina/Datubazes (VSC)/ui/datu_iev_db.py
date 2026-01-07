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
        poga_dalibnieki)

ft.run(main)