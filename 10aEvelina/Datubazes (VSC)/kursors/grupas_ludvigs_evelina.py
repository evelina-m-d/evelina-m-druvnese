import sqlite3
from datetime import datetime, timedelta

savienojums = sqlite3.connect("grupas_ludvigs_evelina.db")
cursor = savienojums.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS kafejnicas(
    kafejnicas_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nosaukums TEXT NOT NULL,
    adrese TEXT NOT NULL,
    atversanas_laiks TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS darbinieki(
    darbinieki_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT NOT NULL,
    uzvards TEXT NOT NULL,
    amats TEXT NOT NULL,
    talrunis TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS produktu_kategorijas(
    kategorijas_id INTEGER PRIMARY KEY AUTOINCREMENT,
    kategorijas_nosaukums TEXT NOT NULL UNIQUE,
    apraksts TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS produkti(
    produkti_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nosaukums TEXT NOT NULL,
    cena REAL NOT NULL,
    kategorijas_id INTEGER NOT NULL,
    FOREIGN KEY (kategorijas_id) REFERENCES produktu_kategorijas(kategorijas_id) ON DELETE CASCADE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS pasutijumi(
    pasutijumi_id INTEGER PRIMARY KEY AUTOINCREMENT,
    kafejnicas_id INTEGER NOT NULL,
    darbinieki_id INTEGER NOT NULL,
    produkts_id INTEGER NOT NULL,
    daudzums INTEGER NOT NULL,
    statuss TEXT NOT NULL,
    datums_laiks TEXT NOT NULL,
    FOREIGN KEY (kafejnicas_id) REFERENCES kafejnicas(kafejnicas_id) ON DELETE CASCADE,
    FOREIGN KEY (darbinieki_id) REFERENCES dabinieki(darbinieki_id) ON DELETE CASCADE,
    FOREIGN KEY (produkts_id) REFERENCES produkti(produkti_id) ON DELETE CASCADE
)
""")

def ievade_jn(teksts):
    while True:
        atbilde = input(teksts).lower()
        if atbilde in ["j", "n"]:
            return atbilde
        print("Ievadi tikai 'j' vai 'n'!")

def ievade_skaitlis(teksts):
    while True:
        try:
            atbilde = int(input(teksts).lower())
            if atbilde <= 0:
                print("Ievadiet pozitīvu skaitli!")
                continue
            return atbilde
        except ValueError:
            print("Ievadiet skaitli")


#kafejnicas ievade
while True:
    print("Kafejnīcas ievade!")
    nosaukums = input("Ievadiet nosaukumu:")
    adrese = input("Ievadiet adresi:")
    atversanas_laiks = input("Ievadiet atvēršanās laiku (HH:MM):")

    cursor.execute("INSERT INTO kafejnicas(nosaukums, adrese, atversanas_laiks) VALUES(?,?,?)", (nosaukums, adrese, atversanas_laiks))
    savienojums.commit()

    turpinat = ievade_jn("Vai vēlaties ievadīt vēl kafejnīcas? (j/n):")
    if turpinat != "j":
        break

while True:
    print("Darbinieku ievade!")
    vards = input("Ievadiet vārdu:")
    uzvards = input("Ievadiet uzvārdu:")
    amats = input("Ievadiet amatu:")
    while True:
        telefons = ievade_skaitlis("Ievadiet telefona nr.:")
        if len(str(telefons)) < 8 or len(str(telefons)) > 12:
            print("Telefona nr. jābūt 8-12 cipariem!")
            continue
        break

    cursor.execute("INSERT INTO darbinieki(vards, uzvards, amats, talrunis) VALUES(?,?,?,?)", (vards, uzvards, amats, telefons))
    savienojums.commit()

    turpinat = ievade_jn("Vai vēlaties ievadīt vēl darbiniekus? (j/n):")
    if turpinat != "j":
        break

while True:
    print("kategoriju ievade!")
    nosaukums = input("Ievadiet produkta kategorijas nosaukumu:")
    apraksts = input("Ievadiet produkta aprakstu:")

    cursor.execute("INSERT INTO produktu_kategorijas(kategorijas_nosaukums, apraksts) VALUES(?,?)", (nosaukums, apraksts))
    savienojums.commit()

    turpinat = ievade_jn("Vai vēlaties ievadīt vēl kategorijas? (j/n):")
    if turpinat != "j":
        break

while True:
    print("Produktu ievade!")
    nosaukums = input("Ievadiet produkta nosaukumu:")
    cena = ievade_skaitlis("Ievadiet cenu:")
    kategorijas_id = ievade_skaitlis("Ievadiet kategorijas id:")

    cursor.execute("INSERT INTO produkti(nosaukums, cena, kategorijas_id) VALUES(?,?,?)", (nosaukums, cena, kategorijas_id))
    savienojums.commit()

    turpinat = ievade_jn("Vai vēlaties ievadīt vēl produktus? (j/n)")
    if turpinat != "j":
        break

while True:
    print("Pasūtījumu ievade!")
    kafejnicas_id = ievade_skaitlis("Ievadiet kafejnīcas id:")
    darbinieki_id = ievade_skaitlis("Ievadiet darbinieka id:")
    produkts_id = ievade_skaitlis("Ievadiet produkta id:")
    daudzums = ievade_skaitlis("ievadiet daudzumu:")
    statuss = input("Ievadiet statusu:")

    datums = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M"),"%Y-%m-%d %H:%M")
    cursor.execute("INSERT INTO pasutijumi(kafejnicas_id, darbinieki_id, produkts_id, daudzums, statuss, datums_laiks) VALUES(?,?,?,?,?,?)", (kafejnicas_id, darbinieki_id, produkts_id, daudzums, statuss, str(datums)))
    savienojums.commit()

    turpinat = ievade_jn("Vai vēlaties ievadīt vēl pasūtījumus? (j/n)")
    if turpinat != "j":
        break


def kafejnicu_dati():
    print("*********************************************************\nKafejnīcas, pēc atvēršanas laika augošā secībā:\n*********************************************************")
    cursor.execute("""
    SELECT * FROM kafejnicas
    ORDER BY atversanas_laiks ASC
    """)
    for i in cursor.fetchall():
        print(f"ID {i[0]} | Nosaukums: {i[1]} | Adrese: {i[2]} | Atvēršanas laiks: {i[3]}")

kafejnicu_dati()

def darbinieku_pasutijumi():
    print("*********************************************************\nDarbinieki un viņu veiktie pasūtījumi:\n*********************************************************")
    cursor.execute("""
    SELECT 
        darbinieki.vards,
        darbinieki.uzvards,
        COUNT(pasutijumi.pasutijumi_id)
    FROM pasutijumi
    LEFT JOIN darbinieki ON pasutijumi.darbinieki_id = darbinieki.darbinieki_id
    GROUP BY darbinieki.vards
    """)
    for i in cursor.fetchall():
        print(f"Darbinieks: {i[0]} {i[1]} | Pasūtījumu skaits: {i[2]}")

darbinieku_pasutijumi()

def produkti_kategorijas():
    print("*********************************************************\nProdukti un to kategorijas:\n*********************************************************")
    cursor.execute("""
    SELECT
        produkti.nosaukums,
        produkti.cena,
        produktu_kategorijas.kategorijas_nosaukums
    FROM produkti
    LEFT JOIN produktu_kategorijas ON produktu_kategorijas.kategorijas_id = produkti.kategorijas_id
    GROUP BY produkti.nosaukums
    """)
    for i in cursor.fetchall():
        print(f"Produkts: {i[0]} | Cena: {i[1]} | Kategorija: {i[2]}")

produkti_kategorijas()

def cetrdesmit_astonas_stundas():
    print("*********************************************************\nPēdējo 48h pasūtījumi:\n*********************************************************")
    cursor.execute("""
    SELECT 
        pasutijumi.*,
        kafejnicas.nosaukums,
        darbinieki.vards,
        darbinieki.uzvards,
        produkti.nosaukums
    FROM pasutijumi
    LEFT JOIN kafejnicas ON kafejnicas.kafejnicas_id = pasutijumi.kafejnicas_id
    LEFT JOIN darbinieki ON darbinieki.darbinieki_id = pasutijumi.darbinieki_id
    LEFT JOIN produkti ON produkti.produkti_id = pasutijumi.produkts_id
    GROUP BY pasutijumi.pasutijumi_id
    """)
    for i in cursor.fetchall():
        datums_txt = i[6]
        datums = datetime.strptime(datums_txt, "%Y-%m-%d %H:%M:%S")
        sodiena = datetime.now()
        aizvakardiena = sodiena - timedelta(days=2) 
        if datums < sodiena and datums > aizvakardiena:
            print(f"Pasūtījuma ID {i[0]} | Kafejnīca: {i[7]} | Darbinieks: {i[8]} {i[9]} | Produkts: {i[10]} | Skaits: {i[4]} | Pasūtījuma laiks: {i[6]}")

cetrdesmit_astonas_stundas()

def popularakie_produkti():
    print("*********************************************************\nPopulārākie produkti:\n*********************************************************")
    cursor.execute("""
    SELECT
        produkti.nosaukums,
        SUM(pasutijumi.daudzums)
    FROM pasutijumi
    LEFT JOIN produkti ON produkti.produkti_id = pasutijumi.produkts_id
    GROUP BY produkti.nosaukums
    HAVING SUM(pasutijumi.daudzums) > 5
    ORDER BY SUM(pasutijumi.daudzums) DESC
    """)
    for i in cursor.fetchall():
        print(f"Produkts: {i[0]} | Skaits: {i[1]}")

popularakie_produkti()

def videja_cena():
    print("*********************************************************\nKategorijas un to vidējā cena:\n*********************************************************")
    cursor.execute("""
    SELECT
        produktu_kategorijas.kategorijas_nosaukums,
        AVG(produkti.cena)
    FROM produktu_kategorijas
    LEFT JOIN produkti ON produkti.kategorijas_id = produktu_kategorijas.kategorijas_id
    GROUP BY produktu_kategorijas.kategorijas_nosaukums
    """)
    for i in cursor.fetchall():
        print(f"Kategorija: {i[0]} | Vidējā cena: {round(i[1])}€")

videja_cena()

def apgrozijums():
    print("*********************************************************\nKafejnīcas un to apgrozījums:\n*********************************************************")
    cursor.execute("""
    SELECT
        kafejnicas.kafejnicas_id,
        kafejnicas.nosaukums,
        pasutijumi.daudzums,
        produkti.cena,
        SUM(pasutijumi.daudzums * produkti.cena)
    FROM pasutijumi
    LEFT JOIN kafejnicas ON pasutijumi.kafejnicas_id = kafejnicas.kafejnicas_id
    LEFT JOIN produkti on produkti.produkti_id = pasutijumi.produkts_id
    GROUP BY kafejnicas.kafejnicas_id
    ORDER BY SUM(pasutijumi.daudzums * produkti.cena) DESC
    """)
    for i in cursor.fetchall():
        print(f"ID {i[0]} | Kafejnīca: {i[1]} | Apgrozījums: {round(i[4])}€")

apgrozijums()

def biezakas_kategorijas():
    print("*********************************************************\nVisbiežāk sūtītās kategorijas (virs 3 pasūtījumiem)\n*********************************************************:")
    cursor.execute("""
    SELECT
        produktu_kategorijas.kategorijas_nosaukums,
        COUNT(pasutijumi.pasutijumi_id)
    FROM pasutijumi
    LEFT JOIN produkti ON produkti.produkti_id = pasutijumi.produkts_id
    LEFT JOIN produktu_kategorijas ON produktu_kategorijas.kategorijas_id = produkti.kategorijas_id
    GROUP BY produktu_kategorijas.kategorijas_nosaukums
    HAVING COUNT(pasutijumi.pasutijumi_id) > 3
    ORDER BY COUNT(pasutijumi.pasutijumi_id) DESC
    """)
    for i in cursor.fetchall():
        print(f"Kategorija: {i[0]} | Pasūtījumu skaits: {i[1]}")

biezakas_kategorijas()