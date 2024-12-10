import csv

#1. uzdevums

def ierakstit():
    with open('file.txt', 'a', encoding='utf-8', newline='') as fails:
        for i in range (1,7):
            ieraksts = (input('Ievadiet savu tekstu:') + '\n')
            fails.write(ieraksts)
    print("Teksts saglabāts!")

#ierakstit()


#2. uzdevums

def nolasit():
    try:
        with open('file.txt', 'r', encoding='utf-8', newline='') as fails:
            dati = fails.readlines()
            print("Teksts failā:")
            for ieraksts in dati:
                    print(ieraksts.strip())
    except FileNotFoundError:
        print("Fails nepastāv!")

#nolasit()


#3. uzdevums

def nolasit_ar_for():
    try:
        with open('file.txt', 'r', encoding='utf-8', newline='') as fails:
            print("Teksts failā:")
            for i in fails:
                print(i.strip())
    except FileNotFoundError:
        print("Fails nepastāv!")

#nolasit_ar_for()


#4. uzdevums

saraksts = ["zīmulis", "dzēšgumija", "lineāls"]

def saraksts_faila(saraksts):
    try:
        with open('file.txt', 'a', encoding='utf-8', newline='') as fails:
            for i in saraksts:
                fails.writelines(i + '\n')

        with open('file.txt', 'r', encoding='utf-8', newline='') as fails:
            print("Teksts failā:\n*******************")
            for i in fails:
                print(i.strip())

        skaits = len(saraksts)
        print(f"*******************\nPievienoti {skaits} vārdi.")

    except FileNotFoundError:
        print("Fails nepastāv!")

#saraksts_faila(saraksts)


#5. uzdevums

def meklet_vardu():
    try:
        with open('file.txt', 'r', encoding='utf-8', newline='') as fails:
            vards = input("Kādu vārdu vēlaties meklēt?:")
            if vards in fails.read():
                print(f"Vārds '{vards}' ir failā!")
            else:
                print(f"Vārds '{vards}' nav failā.")
    except FileNotFoundError:
        print("Fails nepastāv!")

#meklet_vardu()


#6. uzdevums

def seciba():
    try:
        with open('file.txt', 'r', encoding='utf-8', newline='') as fails:
            saturs = fails.readlines()
            kartots = sorted(saturs, reverse=True)
        with open('file.txt', 'w', encoding='utf-8', newline='') as fails:
            fails.writelines(kartots)
    except FileNotFoundError:
        print("Fails nepastāv!")

#seciba()


