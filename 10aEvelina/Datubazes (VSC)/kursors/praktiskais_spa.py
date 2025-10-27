import sqlite3
savienojums=sqlite3.connect("spa_sistema.db")
cursor=savienojums.cursor()

cursor.execute("DROP TABLE IF EXISTS klienti")
cursor.execute("DROP TABLE IF EXISTS pakalpojumi")
cursor.execute("DROP TABLE IF EXISTS pieraksti")

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
        datums TEXT NOT NULL
    )
""")

print("Datubāze un tabulas izveidotas!")

