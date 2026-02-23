
from collections import deque

visas_biletes = [(1, "Anna", "B11"), (2, "Jānis", "A15"), (3, "Jolanta", "B02"), (4, "Rostimirs", "B25"), (5, "Reičela", "A19")]
aiznemtas_sedvietas = {"B11", "A15", "B02", "B25", "A19"}
rinda = deque()

def meklet_bileti(biletes_id, biletes_saraksts):
    visu_bilesu_id = [bilete[0] for bilete in biletes_saraksts]
    if biletes_id in visu_bilesu_id:
        print("Biļete: ", biletes_saraksts[biletes_id - 1])
    else:
        print("Šāda biļete neeksistē!")
    
def pievienot_bileti(biletes_id, pirceja_vards, sedvieta, biletes_saraksts, aiznemtas_sedvietas):
    visu_bilesu_id = [bilete[0] for bilete in biletes_saraksts]
    if biletes_id in visu_bilesu_id:
        print("Biļete ar šādu ID jau eksistē!")
    elif sedvieta in aiznemtas_sedvietas:
        print("Šī sēdvieta jau ir aizņemta!")
    else:
        visas_biletes.append((biletes_id, pirceja_vards, sedvieta))
        print(f"Pievienota sekojošā biļete: ID {biletes_id}, Vārds: {pirceja_vards}, Sēdvieta: {sedvieta}")

def vai_sedvieta_aiznemta(sedvieta, aiznemtas_sedvietas):
    if sedvieta in aiznemtas_sedvietas:
        print("Šī sēdvieta ir aizņemta.")
    else:
        print("Šī sēdvieta nav aizņemta/neeksistē.")

def ienakt_rinda():
    pass

def aiznemto_sedvietu_skaits():
    pass

def izvelne():
    while True:
        print("---------------------------------\nKoncertzāles pārvaldības sistēma\n1 - meklēt biļeti\n2 - pievienot jaunu biļeti\n3 - pārbaudīt, vai sēdvieta ir aizņemta\n4 - ienākt rindā\n5 - skatīt aizņemto sēdvietu skaitu\n6 - iziet no programmas")
        try:
            match int(input("Izvēlies darbību (1-6): ")):
                case 1:
                    while True:
                        print("---------------------------------")
                        try:
                            biletes_id = int(input("Ievadi biļetes ID:"))
                            break
                        except ValueError:
                            print("Ievadi skaitli!")

                    meklet_bileti(biletes_id, visas_biletes)

                case 2:
                    while True:
                        print("---------------------------------")
                        try:
                            biletes_id = int(input("Ievadi biļetes ID:"))
                            pirceja_vards = input("Ievadi vārdu:")
                            sedvieta = input("Ievadi sēdvietu (A01 - A99 vai B01 - B50):")
                            break
                        except ValueError:
                            print("Ievadi skaitli!")

                    pievienot_bileti(biletes_id, pirceja_vards, sedvieta, visas_biletes, aiznemtas_sedvietas)

                case 3:
                    print("---------------------------------")
                    sedvieta = input("Ievadi sēdvietu (A01 - A99 vai B01 - B50):")
                    vai_sedvieta_aiznemta(sedvieta,aiznemtas_sedvietas)
                case 4:
                    ienakt_rinda()
                case 5:
                    aiznemto_sedvietu_skaits()
                case 6:
                    print("Paldies!")
                    break
                case _:
                    raise ValueError
        except ValueError:
            print("Ievadi skaitli no 1-6!")

izvelne()