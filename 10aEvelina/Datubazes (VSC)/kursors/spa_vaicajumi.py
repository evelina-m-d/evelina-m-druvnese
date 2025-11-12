#pieslēgties esošajai datubāzei
#jāuzraksta programma, kur lietotājs var izvēlēties opcijas no 0-5
#katra opcija atgriež vaicājuma rezultātus, bet 0 iziet no programmas
#nevar ievadīt neko citu kā tikai 0-5
#1 - visi klienti
#2 - visi pakalpojumi
#3 - visi pieraksti ar klienta vārdu un pakalpojumu
#4 - tuvāko 7 dienu pieraksti
#5 - lietotājs norāda cenu, parādīt pakalpojumus, kas ir dārgāki

import sqlite3
import datetime
import time

savienojums=sqlite3.connect("spa_sistema.db")
cursor=savienojums.cursor()

def beigt():
    time.sleep(0.5)
    print("Paldies, visu labu!")

def pirma():
    time.sleep(0.5)
    print("****************************\nVisi klienti, kas reģistrēti sistēmā:\n")
    cursor.execute("SELECT * FROM klienti")
    visi=cursor.fetchall()
    for i in visi:
        print(f"ID {i[0]} | Vārds: {i[1]} {i[2]} | Telefona numurs: {i[3]}\n")

def otra():
    time.sleep(0.5)
    print("****************************\nVisi pakalpojumi, kas reģistrēti sistēmā:\n")
    cursor.execute("SELECT * FROM pakalpojumi")
    visi=cursor.fetchall()
    for i in visi:
        print(f"ID {i[0]} | Nosaukums: {i[1]} | Cena: {i[2]}€ | Ilgums, minūtēs: {i[3]}\n")

def tresa():
    time.sleep(0.5)
    print("****************************\nVisi pieraksti, kas reģistrēti sistēmā:")
    cursor.execute("""
    SELECT 
        pieraksti.pieraksta_id,
        klienti.vards,
        klienti.uzvards,
        pakalpojumi.nosaukums,
        pieraksti.datums
    FROM pieraksti
    LEFT JOIN klienti ON klienti.klienti_id = pieraksti.klients
    LEFT JOIN pakalpojumi ON pakalpojumi.pakalpojuma_id = pieraksti.pakalpojums
    GROUP BY pieraksti.pieraksta_id
    """)
    visi=cursor.fetchall()
    for i in visi:
        print(f"Pieraksta ID {i[0]} | Klienta vārds: {i[1]} {i[2]} | Pakalpojums: {i[3]} | Datums: {i[4]}\n")

def ceturta():
    time.sleep(0.5)
    print("****************************\nTuvāko 7 dienu pieraksti:\n")
    cursor.execute("""
    SELECT
        pieraksti.pieraksta_id,
        klienti.vards,
        klienti.uzvards,
        pakalpojumi.nosaukums,
        pieraksti.datums
    FROM pieraksti
    LEFT JOIN klienti ON klienti.klienti_id = pieraksti.klients
    LEFT JOIN pakalpojumi ON pakalpojumi.pakalpojuma_id = pieraksti.pakalpojums
    GROUP BY pieraksti.pieraksta_id
    """)
    for tuple in cursor.fetchall():
        datums_txt = tuple[4]
        datums = datetime.datetime.strptime(datums_txt,"%Y-%m-%d").date()
        sodiena = datetime.datetime.now().date() 
        datums_pec_sept = sodiena + datetime.timedelta(days=7)
        pierakstu_skaits = 0
        if datums > sodiena and datums < datums_pec_sept:
            print(f"Pieraksta ID {tuple[0]} | Klienta vārds: {tuple[1]} {tuple[2]} | Pakalpojums: {tuple[3]} | Datums: {tuple[4]}\n")
            pierakstu_skaits += 1
    if pierakstu_skaits == 0:
        print("Nākamajās 7 dienās nav neviena pieraksta!\n")
    else:
        pass

def piekta():
    while True:
        try:
            time.sleep(0.5)
            liet_cena = float(input("\n****************************\nIevadiet savu budžetu: "))
            time.sleep(0.5)
            if liet_cena > 0:
                print("Visi pakalpojumi, kas ir ārpus jūsu budžeta: \n")
                cursor.execute("SELECT * FROM pakalpojumi")
                visi=cursor.fetchall()
                pakalpojumu_skaits = 0
                for i in visi:
                    cena = i[2]
                    if cena > liet_cena:
                        print(f"Pakalpojums: {i[1]} | Cena: {i[2]}€\n")
                        pakalpojumu_skaits += 1
                    else:
                        pass
                if pakalpojumu_skaits < 1:
                    print("Neviens pakalpojums nav ārpus jūsu budžeta!\n")
                    break
                else:
                    pass
                    break
            else:
                raise ValueError
        except ValueError:
            print("Ievadiet pozitīvu skaitli!")

def ievade():
    while True:
        print("SPA sistēmas apskates programma\n****************************\n")
        print(" 1 - Apskatīt visus klientus\n 2 - Apskatīt visus pakalpojumus\n 3 - Apskatīt visus pierakstus\n 4 - Apskatīt tuvāko 7 dienu pierakstus\n 5 - Apskatīt pakalpojumus, kas neietilpst jūsu budžetā\n 0 - Aizvērt programmu\n")
        try:
            izvelne=int(input("Izvēlaties vēlamo funkciju: "))
            if izvelne == 0:
                beigt()
                break

            elif izvelne == 1:
                pirma()

            elif izvelne == 2:
                otra()

            elif izvelne == 3:
                tresa()

            elif izvelne == 4:
                ceturta()
            
            elif izvelne == 5:
                piekta()
            
            else:
                raise ValueError

        except ValueError:
            print("\n****************************\nIevadiet skaitli no 0 līdz 5!\n****************************\n")
    
ievade()
                        