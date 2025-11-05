import sqlite3
savienojums=sqlite3.connect("spa_sistema.db")
cursor=savienojums.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS klienti (
        klienti_id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT NOT NULL,
        uzvards TEXT NOT NULL,
        tel_numurs TEXT UNIQUE NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pakalpojumi (
        pakalpojuma_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nosaukums TEXT NOT NULL,
        cena REAL NOT NULL,
        ilgums_minutes INTEGER NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pieraksti (
        pieraksta_id INTEGER PRIMARY KEY AUTOINCREMENT,
        klients TEXT NOT NULL,
        pakalpojums TEXT NOT NULL,
        datums TEXT NOT NULL,
        FOREIGN KEY (klients) REFERENCES klienti(klienti_id),
        FOREIGN KEY (pakalpojums) REFERENCES pakalpojumi(pakalpojuma_id)
    )
""")

print("--Pievienot klientu")
vards=input("Ievadi vardu:")
uzvards=input("Ievadi uzvardu")
tel_numurs=input("Ievadi telefona nr:")

cursor.execute("""
    INSERT INTO klienti(vards,uzvards,tel_numurs) VALUES(?,?,?)""",
    (vards, uzvards, tel_numurs)
)
savienojums.commit()
print("Klients pievienots!")

print("--pievienot pakalpojumu")
nosaukums=input("Ievadi pakalpojuma nosaukumu:")
cena=input("Ievadi pakalpojuma cenu:")
ilgums=input("Ievadi pakalpojuma ilgumu:")

cursor.execute("""
    INSERT INTO pakalpojumi(nosaukums,cena,ilgums_minutes) VALUES(?,?,?)""",
    (nosaukums, cena, ilgums)
)
savienojums.commit()

print("Pakalpojums pievienots!")

print("Pieraksta pievienošana -")
klients=input("Klienta id:")
pakalpojums=input("Pakalpojuma id:")
datums=input("Datums:")

cursor.execute("""
    INSERT INTO pieraksti(klients,pakalpojums,datums) VALUES(?,?,?)""",
    (klients, pakalpojums, datums)
)
savienojums.commit()