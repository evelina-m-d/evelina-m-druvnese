import sqlite3
savienojums=sqlite3.connect("skola.db") #automātiski izveido failu, ja tāda nav

#cursor objekts
cursor=savienojums.cursor()

cursor.execute("DROP TABLE IF EXISTS skoleni") #lai testa dati nedublētos

#izveidot tabulu skoleni ar kolonnām id, vards, vecums
cursor.execute("""
    CREATE TABLE IF NOT EXISTS skoleni (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT NOT NULL,
        vecums INTEGER NOT NULL
    )
""")

cursor.execute("INSERT INTO skoleni(vards, vecums) VALUES (?,?)",("Anna", 15))
cursor.execute("INSERT INTO skoleni(vards, vecums) VALUES (?,?)",("Jānis", 17))
cursor.execute("INSERT INTO skoleni(vards, vecums) VALUES (?,?)",("Gunārs", 16))

savienojums.commit() #ievieto datus datubāzē

print("Visi skolēni: ")
cursor.execute("SELECT * FROM skoleni")
visi=cursor.fetchall()
for i in visi:
    print(f"ID: {i[0]} | Vārds: {i[1]} | Vecums: {i[2]}")

print("\nSkolēni, kas jaunāki par 17:")
cursor.execute("SELECT * FROM skoleni WHERE vecums < 17")
jaunie=cursor.fetchall()
for i in jaunie:
    print(f"ID: {i[0]} | Vārds: {i[1]} | Vecums: {i[2]}")

print("\nVecākais skolēns:")
cursor.execute("SELECT * FROM skoleni ORDER BY vecums DESC LIMIT 1")
vecakais=cursor.fetchone()
print(f"{vecakais[1]} ({vecakais[2]} gadi)")

cursor.execute("SELECT COUNT(*) FROM skoleni WHERE vecums < 17")
rez=cursor.fetchone()[0]
print(f"\nJaunāki par 17 gadiem: {rez} skolēni")