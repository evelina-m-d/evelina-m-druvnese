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




while True:
    print("--Pievienot klientu")
    vards=input("Ievadi vardu: ")
    uzvards=input("Ievadi uzvardu: ")
    tel_numurs=input("Ievadi telefona nr: ")

    cursor.execute("""
        INSERT INTO klienti(vards,uzvards,tel_numurs) VALUES(?,?,?)""",
        (vards, uzvards, tel_numurs)
    )

    turpinat=input("Vai vēlaties turpināt pievienot klientus? (j/n)".lower())
    if turpinat != 'j':
        savienojums.commit()
        print("Klients pievienots!")
        break    



while True:
    print("--pievienot pakalpojumu")
    nosaukums=input("Ievadi pakalpojuma nosaukumu:")
    cena=input("Ievadi pakalpojuma cenu:")
    ilgums=input("Ievadi pakalpojuma ilgumu:")

    cursor.execute("""
        INSERT INTO pakalpojumi(nosaukums,cena,ilgums_minutes) VALUES(?,?,?)""",
        (nosaukums, cena, ilgums)
    )
    
    turpinat=input("Vai vēlaties turpināt pievienot pakalpojumus? (j/n)".lower())
    if turpinat != 'j':
        savienojums.commit()
        print("Pakalpojums pievienots!")
        break



while True:
    print("Pieejamie klienti:")
    cursor.execute("SELECT klienti_id, vards, uzvards FROM klienti")
    for klients in cursor.fetchall():
        print(f"ID {klients[0]} - {klients[1]} - {klients[2]}")
    while True: 
        try:
            klients_id=int(input("Ievadi klienta id: "))
            cursor.execute("SELECT COUNT(*) FROM klienti WHERE klienti_id=?", (klients_id,))
            if cursor.fetchone()[0]>0:
                break
            else:
                print("Klients ar šādu ID neeksistē!")
        except ValueError:
            print("Ievadi skaitli, jo ID ir cipars")
    
    
    print("Pieejamie pakalpojumi")
    cursor.execute("SELECT pakalpojuma_id, nosaukums, cena FROM pakalpojumi")
    for p in cursor.fetchall():
        print(f"ID {p[0]} - {p[1]} {p[2]}€")
    while True: 
        try:
            pakalpojuma_id=int(input("Ievadi pakalpojuma id: "))
            cursor.execute("SELECT COUNT(*) FROM pakalpojumi WHERE pakalpojuma_id=?", (pakalpojuma_id,))
            if cursor.fetchone()[0]>0:
                break
            else:
                print("Pakalpojums ar šādu ID neeksistē!")
        except ValueError:
            print("Ievadi skaitli, jo ID ir cipars")

    datums = input("Ievadi pieraksta datumu (YYYY-MM-DD):")
    cursor.execute("""
        INSERT INTO pieraksti(klients,pakalpojums,datums) VALUES(?,?,?)""",
        (klients_id, pakalpojuma_id, datums))
    savienojums.commit()
    turpinat=input("Vai pievienosiet vēl pierakstu? (j/n)".lower())
    if turpinat != "j":
        break


    
print("Visi klienti:")
cursor.execute("SELECT * FROM klienti")
for rinda in cursor.fetchall():
    print(rinda)

print("Visi pakalpojumi:")
cursor.execute("SELECT * FROM pakalpojumi")
for rinda in cursor.fetchall():
    print(rinda)

print("Visi pieraksti:")
cursor.execute("SELECT * FROM pieraksti")
for rinda in cursor.fetchall():
    print(rinda)

