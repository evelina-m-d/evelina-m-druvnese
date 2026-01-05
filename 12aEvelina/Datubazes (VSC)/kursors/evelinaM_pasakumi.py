import sqlite3
import datetime
import time

savienojums = sqlite3.connect("evelinaM_pasakumi.db") #izveido savienojumu ar sql datubāzi, ja nav datubāzes, tad izveido
cursor = savienojums.cursor()

#izveido atbilstošās tabulas, ja tās jau nepastāv

cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS pasakumi (
        pasakumi_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nosaukums TEXT NOT NULL,
        datums TEXT NOT NULL,
        vieta TEXT NOT NULL
    )
""") 

cursor.execute("""
    CREATE TABLE IF NOT EXISTS dalibnieki (
        dalibnieki_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        vards TEXT NOT NULL,
        uzvards TEXT NOT NULL,
        vecums INTEGER NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS registracijas (
        registracijas_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        pasakumi_id INTEGER NOT NULL,
        dalibnieki_id INTEGER NOT NULL,
        statuss TEXT NOT NULL,
        FOREIGN KEY (pasakumi_id) REFERENCES pasakumi(pasakumi_id),
        FOREIGN KEY (dalibnieki_id) REFERENCES dalibnieki(dalibnieki_id)
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

def ievade_datums(teksts): #datumu pārbaudes funkcija
    try:
        datums=datetime.datetime.strptime(teksts,"%Y-%m-%d").date()
        if datums < datetime.datetime.now().date():
            print("Datums nevar būt pagātnē!")
            ievade_datums(ievade_tuksa("Ievadiet datumu YYYY-MM-DD formātā: "))
        else:
            return datums
    except ValueError:
        print("Nepareizs formāts!")
        ievade_datums(ievade_tuksa("Ievadiet datumu YYYY-MM-DD formātā: "))

def ievade_vecums(teksts):
    while True:
        try:
            atbilde=int(teksts)
            if atbilde < 0:
                print("Skaitlim jābūt pozitīvam!")
                ievade_vecums(ievade_tuksa("Ievadiet dalībnieka vecumu: "))
            else:
                return atbilde
        except ValueError:
            print("Jābūt skaitlim!")
            ievade_vecums(ievade_tuksa("Ievadiet dalībnieka vecumu: "))
    
iteracijas = 0

while True:
    try:
        print("\nPasākumu un dalībnieku reģistrācijas programma\n****************************************")
        print("1 - Ievadīt jaunu pasākumu")
        print("2 - Ievadīt jaunu dalībnieku")
        print("3 - Ievadīt jaunu reģistrāciju\n****************************************")
        print("4 - Apskatīt visus pasākumus")
        print("5 - Apskatīt visus dalībniekus, kas vecāki par 17 gadiem")
        print("6 - Apskatīt visus dalībniekus un viņu reģistrācijas pasākumos")
        print("7 - Apskatīt Dalībnieku skaitu katrā pasākumā")
        print("8 - Apskatīt pasākumus, kuru apmeklētība ir > 3")
        print("9 - Apskatīt 3 apmeklētākos pasākumus \n****************************************")
        print("0 - Iziet no programmas\n****************************************")
        ievade = int(input("Ievadiet vēlamo funkciju: "))
        if ievade == 1:
            while True:
                
                nosaukums = ievade_tuksa("Ievadiet pasākuma nosaukumu: ")
                datums = ievade_datums(ievade_tuksa("Ievadiet datumu YYYY-MM-DD formātā: "))
                vieta = ievade_tuksa("Ievadiet pasākuma atrašanās vietu: ")

                cursor.execute("""
                    INSERT INTO pasakumi(nosaukums,datums,vieta) VALUES(?,?,?)""", #ieraksta datus datubāzē
                    (nosaukums, datums, vieta)
                )
                savienojums.commit()

                iteracijas += 1
                if iteracijas == 2:
                    turpinat = ievade_jn("Vai vēlaties turpināt ievadīt pasākumus?: ")
                    if turpinat == "n":
                        iteracijas = 0
                        break
                    else:
                        iteracijas = 0
                        pass

        elif ievade == 2:

            while True:
                vards = ievade_tuksa("Ievadiet dalībnieka vārdu: ")
                uzvards = ievade_tuksa("Ievadiet dalībnieka uzvārdu: ")
                vecums = ievade_vecums(ievade_tuksa("Ievadiet dalībnieka vecumu: "))

                cursor.execute("""
                    INSERT INTO dalibnieki(vards,uzvards,vecums) VALUES(?,?,?)""", #ieraksta datus datubāzē
                    (vards, uzvards, vecums)
                )
                savienojums.commit()

                iteracijas += 1
                if iteracijas == 2:
                    turpinat = ievade_jn("Vai vēlaties turpināt ievadīt dalībniekus?: ")
                    if turpinat == "n":
                        iteracijas = 0
                        break
                    else:
                        iteracijas = 0
                        pass

        elif ievade == 3:
            
            while True:

                print("Pieejamie dalībnieki:")
                cursor.execute("SELECT dalibnieki_id, vards, uzvards FROM dalibnieki")
                for dalibnieki in cursor.fetchall():
                    print(f"ID {dalibnieki[0]} - {dalibnieki[1]} - {dalibnieki[2]}")
                while True: 
                    try:
                        dalibnieki_id=int(ievade_tuksa("Ievadi dalībnieka id: "))
                        cursor.execute("SELECT COUNT(*) FROM dalibnieki WHERE dalibnieki_id=?", (dalibnieki_id,))
                        if cursor.fetchone()[0]>0:
                            break
                        else:
                            print("Dalībnieks ar šādu ID neeksistē!")
                    except ValueError:
                        print("Ievadi skaitli, jo ID ir cipars!")
                
                
                print("Pieejamie pasākumi:")
                cursor.execute("SELECT pasakumi_id, nosaukums, datums, vieta FROM pasakumi")
                for pasakumi in cursor.fetchall():
                    print(f"ID {pasakumi[0]} - {pasakumi[1]}, {pasakumi[2]}, {pasakumi[3]}")
                while True: 
                    try:
                        pasakumi_id=int(ievade_tuksa("Ievadi pasākuma id: "))
                        cursor.execute("SELECT COUNT(*) FROM pasakumi WHERE pasakumi_id=?", (pasakumi_id,))
                        if cursor.fetchone()[0]>0:
                            break
                        else:
                            print("Pasākums ar šādu ID neeksistē!")
                    except ValueError:
                        print("Ievadi skaitli, jo ID ir cipars!")

                statuss = ievade_tuksa("Ievadiet reģistrācijas statusu (pieņemta/procesā/nepieņemta): ")

                cursor.execute("""
                    INSERT INTO registracijas(pasakumi_id,dalibnieki_id,statuss) VALUES(?,?,?)""", #ieraksta datus datubāzē
                    (pasakumi_id, dalibnieki_id, statuss)
                )
                savienojums.commit()

                iteracijas += 1
                if iteracijas == 2:
                    turpinat = ievade_jn("Vai vēlaties turpināt ievadīt reģistrācijas?: ")
                    if turpinat == "n":
                        iteracijas = 0
                        break
                    else:
                        iteracijas = 0
                        pass

        elif ievade == 4:

            print("Visi pasākumi:")
            cursor.execute("""
            SELECT * FROM pasakumi
            """)

            for i in cursor.fetchall():
                print(f"\nID: {i[0]} | Nosaukums: {i[1]} | Datums: {i[2]} | Vieta: {i[3]}")

        elif ievade == 5:

            print("Visi dalībnieki, kas vecāki par 17:")
            cursor.execute("""
            SELECT * FROM dalibnieki
            WHERE vecums > 17
            GROUP BY vecums
            """)

            for i in cursor.fetchall():
                print(f"\nID: {i[0]} | Vārds: {i[1]} {i[2]} | Vecums: {i[3]}")

        elif ievade == 6:

            print("Dalībnieki un viņu reģistrētie pasākumi:")
            cursor.execute("""
            SELECT
                registracijas.registracijas_id,
                dalibnieki.vards,
                dalibnieki.uzvards,
                pasakumi.nosaukums
            FROM registracijas
            LEFT JOIN pasakumi ON pasakumi.pasakumi_id = registracijas.pasakumi_id
            LEFT JOIN dalibnieki ON dalibnieki.dalibnieki_id = registracijas.dalibnieki_id
            GROUP BY registracijas.registracijas_id
            ORDER BY dalibnieki.vards
            """)

            for i in cursor.fetchall():
                print(f"\nVārds: {i[1]} {i[2]} | Pasākums: {i[3]}")

        elif ievade == 7:

            print("Pasākumi un to dalībnieku skaits:")
            cursor.execute("""
            SELECT
                pasakumi.nosaukums,
                COUNT(registracijas.dalibnieki_id)
            FROM registracijas
            LEFT JOIN pasakumi ON pasakumi.pasakumi_id = registracijas.pasakumi_id
            LEFT JOIN dalibnieki ON dalibnieki.dalibnieki_id = registracijas.dalibnieki_id
            GROUP BY pasakumi.nosaukums
            """)

            for i in cursor.fetchall():
                print(f"\nPasākums: {i[0]} | Dalībnieku skaits: {i[1]}")

        elif ievade == 8:

            print("Pasākumi, kuru apmeklētība ir > 3:")
            cursor.execute("""
            SELECT
                pasakumi.nosaukums,
                COUNT(registracijas.dalibnieki_id)
            FROM registracijas
            LEFT JOIN pasakumi ON pasakumi.pasakumi_id = registracijas.pasakumi_id
            LEFT JOIN dalibnieki ON dalibnieki.dalibnieki_id = registracijas.dalibnieki_id
            GROUP BY pasakumi.nosaukums
            HAVING COUNT(registracijas.dalibnieki_id) > 3
            """)

            for i in cursor.fetchall():
                print(f"\nPasākums: {i[0]} | Dalībnieku skaits: {i[1]}")

        elif ievade == 9:
            
            print("TOP 3 pasākumi pēc apmeklētības:")
            cursor.execute("""
            SELECT
                pasakumi.nosaukums,
                COUNT(registracijas.dalibnieki_id)
            FROM registracijas
            LEFT JOIN pasakumi ON pasakumi.pasakumi_id = registracijas.pasakumi_id
            LEFT JOIN dalibnieki ON dalibnieki.dalibnieki_id = registracijas.dalibnieki_id
            GROUP BY pasakumi.nosaukums
            ORDER BY COUNT(registracijas.dalibnieki_id) DESC
            """)

            saraksts = cursor.fetchall()
            print(f"\nPasākums: {saraksts[0][0]} | Dalībnieku skaits: {saraksts[0][1]}")
            print(f"\nPasākums: {saraksts[1][0]} | Dalībnieku skaits: {saraksts[1][1]}")
            print(f"\nPasākums: {saraksts[2][0]} | Dalībnieku skaits: {saraksts[2][1]}")

        elif ievade == 0:
            time.sleep(1)
            print("Paldies!")
            break
        else:
            raise ValueError
    except ValueError:
        print("Ievadei ir jābūt skaitlim 0 - 9!")