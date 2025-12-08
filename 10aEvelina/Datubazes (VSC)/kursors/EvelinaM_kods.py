import sqlite3
import datetime

#Datubāzes izveide – pareiza
savienojums = sqlite3.connect("EvelinaM_sutijumi.db")
cursor = savienojums.cursor()

#tabulas ir pieteikami korektas, lai Tev nebūtu jālabo

cursor.execute("""
CREATE TABLE IF NOT EXISTS klienti(
    klienta_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT NOT NULL,
    telefons TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sutijumi(
    sutijuma_id INTEGER PRIMARY KEY AUTOINCREMENT,
    klienta_id INTEGER NOT NULL,
    svars_kg REAL NOT NULL CHECK(svars_kg > 0),
    kategorija TEXT NOT NULL,
    FOREIGN KEY (klienta_id) REFERENCES klienti(klienta_id) ON DELETE CASCADE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS statusi(
    statusa_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sutijuma_id INTEGER NOT NULL,
    apraksts TEXT NOT NULL,
    datums TEXT NOT NULL,
    FOREIGN KEY (sutijuma_id) REFERENCES sutijumi(sutijuma_id) ON DELETE CASCADE
)
""")
savienojums.commit()

#sākumā pārliecināmies, vai tabulā jau ir dati(ja ir, tad neliek, lai šie testa dati netiku dublēti)
cursor.execute("SELECT COUNT(*) FROM klienti")
if cursor.fetchone()[0] == 0:
    klienti = [
        ("Anna", "22334455"),
        ("Jānis", "29998877"),
        ("Laura", "24445566"),
        ("Mārtiņš", "27776655"),
        ("Zane", "25553322")
    ]
    cursor.executemany(
        "INSERT INTO klienti(vards, telefons) VALUES (?, ?)", klienti
    )

cursor.execute("SELECT COUNT(*) FROM sutijumi")
if cursor.fetchone()[0] == 0:
    sutijumi = [
        (1, 2.5, "elektronika"),
        (2, 1.0, "apģērbi"),
        (3, 4.2, "kosmētika"),
        (4, 0.8, "elektronika"),
        (5, 3.6, "apģērbi")
    ]
    cursor.executemany(
        "INSERT INTO sutijumi(klienta_id, svars_kg, kategorija) VALUES (?, ?, ?)",
        sutijumi
    )


cursor.execute("SELECT COUNT(*)FROM statusi")
if cursor.fetchone()[0] == 0:
    statusi = [
        (1, "Pieņemts", "2025-01-10"),
        (2, "Ceļā", "2025-01-11"),
        (3, "Izsniegts", "2025-01-15"),
        (4, "Ceļā", "2025-01-16"),
        (5, "Pieņemts", "2025-01-17")
    ]
    cursor.executemany(
        "INSERT INTO statusi(sutijuma_id, apraksts, datums) VALUES (?, ?, ?)",
        statusi
    )

savienojums.commit()
#uzrakstīt funkcijas pēc noteiktajiem kritērijeim
 
#--------------------------------------------------------------------------------------------------------------------------------------------
#PĀRBAUDES FUNKCIJAS

def parbaude_jn(teksts): #j/n pārbaudes funkcija
    while True:
        atbilde = input(teksts).lower()
        if atbilde in ["j", "n"]:
            return atbilde
        print("Ievadi tikai 'j' vai 'n'!")
 
def parbaude_skaitlis(teksts): #skaitļu pārbaudes funkcija
    while True:
        try:
            atbilde = int(input(teksts).lower())
            if atbilde <= 0:
                print("Ievadiet pozitīvu skaitli!")
                continue
            return atbilde
        except ValueError:
            print("Ievadiet skaitli!")

def parbaude_tuksa(teksts): #tukšu teksta lauciņu pārbaudes funkcija
    while True:
        atbilde=input(teksts)
        if len(atbilde) < 1:
            print("Nedrīkst būt tukšs!")
        else:
            return atbilde

def parbaude_datums(teksts): #datumu pārbaudes funkcija
    try:
        datums=datetime.datetime.strptime(teksts,"%Y-%m-%d").date()
        return datums
    except ValueError:
        print("Nepareizs formāts!")
        parbaude_datums(parbaude_tuksa("Ievadiet datumu YYYY-MM-DD formātā: "))

#-----------------------------------------------------------------------------------------------------------------------------------------------
#IEVADES FUNKCIJAS

def ievadi_klientu():
    while True:
        print("Klientu ievade")
        vards = parbaude_tuksa("Klienta vārds:")
        while True:
            telefons = parbaude_skaitlis("Klienta telefona nr.:")
            if len(str(telefons)) < 8 or len(str(telefons)) > 12:
                print("Telefona nr. jābūt 8-12 cipariem!")
                continue
            break
        
        cursor.execute("INSERT INTO klienti(vards, telefons) VALUES(?,?)", (vards, telefons))
        savienojums.commit()

        turpinat = parbaude_jn("Vai vēlaties ievadīt vēl klientus? (j/n):")
        if turpinat != "j":
            break

#ievadi_klientu()

def ievadi_sutijumu():
    while True:
        print("Sūtījuma ievade:")
        print("Pieejamie klienti:")
        cursor.execute("SELECT klienta_id, vards FROM klienti")
        for klienti in cursor.fetchall():
            print(f"ID {klienti[0]} - {klienti[1]}")
        while True: 
            try:
                klienta_id=int(parbaude_tuksa("Sūtījuma klienta id: "))
                cursor.execute("SELECT COUNT(*) FROM klienti WHERE klienta_id=?", (klienta_id,))
                if cursor.fetchone()[0]>0:
                    break
                else:
                    print("Klients ar šādu ID neeksistē!")
            except ValueError:
                print("Ievadi skaitli, jo ID ir cipars!")
            
        while True:
            try:
                svars = float(parbaude_tuksa("Sūtījuma svars (kg):"))
                if svars < 0:
                    raise ValueError
                else: 
                    break
            except ValueError:
                print("Svaram ir jābūt pozitīvam skaitlim!")
        
        kategorija = parbaude_tuksa("Sūtījuma kategorija (elektronika, apģērbi, kosmētika):")

        cursor.execute("INSERT INTO sutijumi(klienta_id, svars_kg, kategorija) VALUES(?,?,?)", (klienta_id, svars, kategorija))
        savienojums.commit()

        turpinat = parbaude_jn("Vai vēlaties ievadīt vēl sūtījumus? (j/n):")
        if turpinat != "j":
            break

#ievadi_sutijumu()

def ievadi_statusu():
    while True:
        print("Statusa ievade:")
        print("Pieejamie sūtījumi:")
        cursor.execute("""
        SELECT 
            sutijumi.*, 
            klienti.vards 
        FROM sutijumi
        LEFT JOIN klienti ON klienti.klienta_id = sutijumi.klienta_id
        GROUP BY sutijumi.sutijuma_id
        """)
        for sutijumi in cursor.fetchall():
            print(f"ID {sutijumi[0]} - {sutijumi[4]}, {sutijumi[2]}kg, {sutijumi[3]}")
        while True: 
            try:
                sutijuma_id=int(parbaude_tuksa("Sūtījuma id: "))
                cursor.execute("SELECT COUNT(*) FROM sutijumi WHERE sutijuma_id=?", (sutijuma_id,))
                if cursor.fetchone()[0]>0:
                    break
                else:
                    print("Sūtījums ar šādu ID neeksistē!")
            except ValueError:
                print("Ievadi skaitli, jo ID ir cipars!")
        
        statuss = parbaude_tuksa("Sūtījuma statuss:")
        datums = parbaude_datums(parbaude_tuksa("Ievadiet datumu YYYY-MM-DD formātā: "))

        cursor.execute("INSERT INTO statusi(sutijuma_id, apraksts, datums) VALUES(?,?,?)", (sutijuma_id, statuss, datums))
        savienojums.commit()

        turpinat = parbaude_jn("Vai vēlaties ievadīt vēl statusus? (j/n):")
        if turpinat != "j":
            break

#ievadi_statusu()

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#KĻŪDU LABOJUMS
#zemāk dotas nepareizi uzrakstītas funkcijas datu dzēšanai un atjaunināšanai
#ieraksti komentāros, kas tika labots

def dzest_klientu(cursor, savienojums):
    print("Dzēst klientu: ")
    cursor.execute("SELECT klienta_id, vards FROM klienti")
    for klienti in cursor.fetchall():
        print(f"ID {klienti[0]} - {klienti[1]}")
    while True: 
        try:
            klienta_id=int(parbaude_tuksa("Klienta id: "))
            cursor.execute("SELECT COUNT(*) FROM klienti WHERE klienta_id=?", (klienta_id,))
            if cursor.fetchone()[0]>0:
                break
            else:
                print("Klients ar šādu ID neeksistē!")
        except ValueError:
            print("Ievadi skaitli, jo ID ir cipars!")

    #kļūda
    cursor.execute("SELECT * FROM klienti WHERE klienta_id = ?", (klienta_id,)) #vārds 'kursors' tika aizvietots ar 'cursor', parametrizēts vaicājums
    dati=cursor.fetchone() #fetchall aizvietots ar fetchone

    if dati==[]:
        print("Nav atrasts! Tiks dzēsts tāpat!")

    #kļūda
    apstiprinajums=parbaude_jn("Dzēst? j/n: ") #izveidota īsta j/n pārbaude
    if apstiprinajums == 'j':
        #kļūda
        cursor.execute("DELETE FROM klienti WHERE klienta_id =?", (klienta_id,)) #parametrizēts vaicājums
        savienojums.commit()
        #kļūda
        print("Dzēsts!")
    else:
        print("Dzēšana atcelta!")

#dzest_klientu(cursor, savienojums)


def labot_klientu_datus(cursor, savienojums):
    print("Labot klienta datus: ")
    cursor.execute("SELECT klienta_id, vards FROM klienti")
    for klienti in cursor.fetchall():
        print(f"ID {klienti[0]} - {klienti[1]}")
    while True: 
        try:
            klienta_id=int(parbaude_tuksa("Klienta id: "))
            cursor.execute("SELECT COUNT(*) FROM klienti WHERE klienta_id=?", (klienta_id,))
            if cursor.fetchone()[0]>0:
                break
            else:
                print("Klients ar šādu ID neeksistē!")
        except ValueError:
            print("Ievadi skaitli, jo ID ir cipars!")

    #kļūda, vārds 'kursors' tika aizvietots ar 'cursor'
    cursor.execute("SELECT vards FROM klienti WHERE klienta_id =?", (klienta_id,)) #parametrizēts vaicājums
    dati=cursor.fetchone()  #kļūda, vārds 'kursors' tika aizvietots ar 'cursor' un 'fetchall' ar 'fetchone'

    print("Pašreizējais:", dati)

    jaunais_vards=parbaude_tuksa("Jaunais vārds: ")

    #kļūda
    cursor.execute(f"UPDATE klienti SET vards=? WHERE klienta_id=?", (jaunais_vards, klienta_id)) #parametrizēts vaicājums
    savienojums.commit()

    print("Labots!")
    #kļūda

#labot_klientu_datus(cursor, savienojums)

#-----------------------------------------------------------------------------------------------------------------------------------------------
#VAICĀJUMU FUNKCIJAS

def sutijumu_skaits(): #apskatīt šo vaicājumu
    print("Klientu sūtījumu skaits:")
    cursor.execute("""
    SELECT
        klienti.vards,
        COALESCE(COUNT(sutijumi.sutijuma_id), 0) 
    FROM sutijumi
    LEFT JOIN klienti ON klienti.klienta_id = sutijumi.klienta_id
    GROUP BY klienti.vards
    """)
    for i in cursor.fetchall():
        print(f"Vārds: {i[0]} | Sūtījumu skaits: {i[1]}")

#sutijumu_skaits()

def videjais_svars():
    print("Vidējais pasūtījumu svars katram klientam:")
    cursor.execute("""
    SELECT
        klienti.vards,
        AVG(sutijumi.svars_kg)
    FROM sutijumi
    LEFT JOIN klienti ON klienti.klienta_id = sutijumi.klienta_id
    GROUP BY klienti.vards
    """)
    for i in cursor.fetchall():
        print(f"Vārds: {i[0]} | Vidējais sūtījumu svars: {i[1]}kg")

#videjais_svars()

def statusi():
    print("Klienti un to sūtījumu statusi:")
    cursor.execute("""
    SELECT
        statusi.statusa_id,
        statusi.apraksts,
        klienti.vards, 
        sutijumi.svars_kg
    FROM statusi
    LEFT JOIN sutijumi ON sutijumi.sutijuma_id = statusi.sutijuma_id
    LEFT JOIN klienti ON klienti.klienta_id = sutijumi.klienta_id
    GROUP BY statusi.statusa_id
    """)
    for i in cursor.fetchall():
        print(f"Statusa ID: {i[0]} | Statuss: {i[1]} | Klients: {i[2]} | Svars: {i[3]}kg")

#statusi()

#nepieciešams nodrošināt arī izvēlni
def izvelne():
    while True:
        print("1 - Pievienot klientu\n2 - Pievienot sūtījumu\n3 - Pievienot statusu\n4 - Dzēst klientu\n5 - Labot klienta datus\n6 - Apskatīt klienta sūtījumu skaitu\n7 - Apskatīt klienta vidējo sūtījumu svaru\n8 - Apskatīt visu sūtījumu statusus\n0-iziet")
        izvele = input("Izvēlies darbību: ").strip()

        if izvele == "1":
            ievadi_klientu()
        elif izvele == "2":
            ievadi_sutijumu()
        elif izvele == "3":
            ievadi_statusu()
        elif izvele == "4":
            dzest_klientu(cursor, savienojums)
        elif izvele == "5":
            labot_klientu_datus(cursor, savienojums)
        elif izvele == "6":
            sutijumu_skaits()
        elif izvele == "7":
            videjais_svars()
        elif izvele == "8":
            statusi()
        elif izvele == "0":
            print("Programma beidzas.")
            break
        else:
            print("Nederīga izvēle! Mēģini vēlreiz.")

izvelne()