import sqlite3
import time

savienojums = sqlite3.connect("evelinamd_sports.db") #izveido savienojumu ar sql datubāzi, ja nav datubāzes, tad izveido
cursor = savienojums.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS sportisti (
        sportists_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        vards TEXT NOT NULL,
        uzvards TEXT NOT NULL,
        vecums INTEGER NOT NULL
    )
""") #izveido datubāzē tabulas, ja tādas tur jau nepastāv

cursor.execute("""
    CREATE TABLE IF NOT EXISTS nodarbibas (
        nodarbibas_id INTEGER PRIMARY KEY AUTOINCREMENT,
        sportists_id INTEGER NOT NULL,
        veids TEXT NOT NULL,
        ilgums_min INTEGER NOT NULL
    )
""")


def ievade_jn(teksts): #j/n pārbaudes funkcija
    while True:
        atbilde=input(teksts).lower()
        if atbilde in ["j", "n"]:
            return atbilde
        print("Ievadi tikai 'j' vai 'n'!")

def ievade_tuksa(teksts): #tukšu teksta lauciņu pārbaudes funkcija
    while True:
        atbilde=input(teksts)
        if len(atbilde) < 1:
            print("Nedrīkst būt tukšs!")
        else:
            return atbilde


while True:
    print("Sporta nodarbību sistēma\n**********************")
    print("\n1 - Pievienot sportistu \n2 - Pievienot nodarbību \n3 - Katra sportista kopējais nodarbību skaits \n4 - Visi sportisti, kas trenējušies vismaz 120 minūtes \n5 - TOP 3 sportisti pēc pavadītā laika nodarbībās \n0 - Iziet no programmas")
    try:
        izvelne = int(input("Izvēlies darbību: "))
        if izvelne == 1:
            while True:
                print("**********************\n--Pievienot sportistu")
                vards=ievade_tuksa("Ievadi sportista vārdu: ") #izmanto tukšas ievades pārbaudes funkciju

                uzvards=ievade_tuksa("Ievadi sportista uzvārdu: ")

                while True:
                    try:
                        vecums=int(input("Ievadi vecumu: ")) #pārbauda, vai sportists ir virs 5 gadu vecuma un vai ievadītais vecums ir pozitīvs
                        if vecums < 5:
                            raise ValueError
                        else:
                            break
                    except ValueError:
                        print("Sportista vecumam ir jābūt apaļam skaitlim, kas lielāks par 5!")

                cursor.execute("""
                    INSERT INTO sportisti(vards,uzvards,vecums) VALUES(?,?,?)""", #ieraksta datus datubāzē
                    (vards, uzvards, vecums)
                )
                savienojums.commit() 

                turpinat=ievade_jn("Vai vēlaties turpināt pievienot sportistus? (j/n)".lower()) #izmanto j/n pārbaudes funkciju
                if turpinat != 'j':
                    print("Sportists pievienots!")
                    break 

        elif izvelne == 2:
            while True:
                print("**********************\n--Pievienot nodarbību")
                while True:
                    try:
                        sportists_id=int(input("Ievadi sportista id: "))
                        cursor.execute("SELECT COUNT(*) FROM sportisti WHERE sportists_id=?", (sportists_id,)) #pārbauda, vai ievadītais sportista id eksistē
                        if cursor.fetchone()[0]>0:
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("ID ir jābūt pozitīvam skaitlim, kas atbilst kādam esošam sportistam!")

                veids=ievade_tuksa("Ievadi nodarbības veidu: ")

                while True:
                    try:
                        ilgums_min=int(input("Ievadi ilgumu (minūtēs): ")) #pārbauda, vai ievadītās minūtes ir pozitīvas
                        if ilgums_min < 1:
                            raise ValueError
                        else:
                            break
                    except ValueError:
                        print("Nodarbības ilgumam ir jābūt pozitīvam, veselam skaitlim!")

                cursor.execute("""
                    INSERT INTO nodarbibas(sportists_id,veids,ilgums_min) VALUES(?,?,?)""", #ievieto datus datubāzē
                    (sportists_id, veids, ilgums_min)
                )
                savienojums.commit()

                turpinat=ievade_jn("Vai vēlaties turpināt pievienot nodarbības? (j/n)".lower()) #izmanto j/n pārbaudes funkciju
                if turpinat != 'j':
                    print("Nodarbība pievienota!")
                    break 
        
        elif izvelne == 3: 
            print("Visi sportisti un viņu apmeklēto nodarbību skaits:")
            cursor.execute(""" 
            SELECT
                sportisti.vards,
                sportisti.uzvards,
                COUNT(nodarbibas.nodarbibas_id)
            FROM sportisti
            LEFT JOIN nodarbibas ON nodarbibas.sportists_id = sportisti.sportists_id
            GROUP BY sportisti.sportists_id
            """)                                                                      #tiek piekļūts datubāzes datiem
            for i in cursor.fetchall():
                print(f"\nVārds: {i[0]} {i[1]} | Nodarbību skaits: {i[2]}")           #lietotājam parāda atrastos datus no datubāzes
        
        elif izvelne == 4:
            print("Visi sportisti, kas sportojuši vismaz 120 minūtes:") #tiek piekļūts datubāzes datiem
            cursor.execute("""
            SELECT
                sportisti.sportists_id,
                sportisti.vards,
                sportisti.uzvards,
                SUM(nodarbibas.ilgums_min)
            FROM sportisti
            LEFT JOIN nodarbibas ON nodarbibas.sportists_id = sportisti.sportists_id
            GROUP BY sportisti.sportists_id
            """)
            for i in cursor.fetchall():
                if i[3] > 120:
                    print(f"\nVārds: {i[1]} {i[2]} | Sportošanas ilgums: {i[3]}") #lietotājam parāda atrastos datus no datubāzes
                else:
                    pass
        
        elif izvelne == 5:
            print("TOP 3 sportisti, pēc sportošanas kopējā ilguma:")  #tiek piekļūts datubāzes datiem
            cursor.execute("""
            SELECT
                sportisti.sportists_id,
                sportisti.vards,
                sportisti.uzvards,
                SUM(nodarbibas.ilgums_min) AS kopejais_ilgums
            FROM sportisti
            LEFT JOIN nodarbibas ON nodarbibas.sportists_id = sportisti.sportists_id
            GROUP BY sportisti.sportists_id
            ORDER BY kopejais_ilgums DESC
            """)
            saraksts=cursor.fetchall() #lietotājam parāda atrastos datus no datubāzes
            print(f"\nVārds: {saraksts[0][1]} {saraksts[0][2]} | Sportošanas ilgums: {saraksts[0][3]}")
            print(f"\nVārds: {saraksts[1][1]} {saraksts[1][2]} | Sportošanas ilgums: {saraksts[1][3]}")
            print(f"\nVārds: {saraksts[2][1]} {saraksts[2][2]} | Sportošanas ilgums: {saraksts[2][3]}")

        elif izvelne == 0:
            print("Visu labu!")   
            break    

        else:
            raise ValueError
    except ValueError:
        print("\nIevadiet skaitli no 0 līdz 5!\n")
