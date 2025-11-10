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

savienojums=sqlite3.connect("spa_sistema.db")
cursor=savienojums.cursor()

while True:
    print("SPA sistēmas apskates programma\n****************************\n")
    print(" 1 - Apskatīt visus klientus\n 2 - Apskatīt visus pakalpojumus\n 3 - Apskatīt visus pierakstus\n 4 - Apskatīt tuvāko 7 dienu pierakstus\n 5 - Apskatīt pakalpojumus, kas neietilpst jūsu budžetā\n 0 - Aizvērt programmu\n")
    
    izvelne=int(input("Izvēlaties vēlamo funkciju:"))
    if izvelne == 0:
        break
    elif izvelne == 1:
        print("Visi klienti, kas reģistrēti sistēmā:\n")
        cursor.execute("SELECT * FROM klienti")
        visi=cursor.fetchall()
        for i in visi:
            print(f"ID {i[0]} | Vārds: {i[1]} {i[2]} | Telefona numurs: {i[3]}\n")
    elif izvelne == 2:
        print("Visi pakalpojumi, kas reģistrēti sistēmā:\n")
        cursor.execute("SELECT * FROM pakalpojumi")
        visi=cursor.fetchall()
        for i in visi:
            print(f"ID {i[0]} | Nosaukums: {i[1]} | Cena: {i[2]}€ | Ilgums, minūtēs: {i[3]}\n")
    elif izvelne == 3:
        print("Visi pieraksti, kas reģistrēti sistēmā:")
        cursor.execute("""
        SELECT 
            pieraksti.pieraksta_id,
            klienti.vards,
            klienti.uzvards,
            pakalpojumi.nosaukums
        FROM pieraksti
        LEFT JOIN klienti ON klienti.klienti_id = pieraksti.klients
        LEFT JOIN pakalpojumi ON pakalpojumi.pakalpojuma_id = pieraksti.pakalpojums
        GROUP BY pieraksti.pieraksta_id
        """)
        visi=cursor.fetchall()
        for i in visi:
            print(f"Pieraksta ID {i[0]} | Klienta vārds: {i[1]} {i[2]} | Pakalpojums: {i[3]}\n")
    elif izvelne == 4:
        print("Tuvāko 7 dienu pieraksti:")