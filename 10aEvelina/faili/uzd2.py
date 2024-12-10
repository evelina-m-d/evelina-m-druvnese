#7. uzdevums

import csv

def izveidot_csv():
    with open('file.csv', 'w', encoding='utf-8', newline='') as fails:
        rakstitajs = csv.writer(fails)
        rakstitajs.writerow(["ID", "Name", "Age"])
        rakstitajs.writerows([[1, "Alise", 25], [2, "Jānis", 18], [3, "Ance", 39]])
    print("Fails ir izveidots!")

#izveidot_csv()


#8. uzdevums

def lasit_csv():
    try:
        with open('file.csv', 'r', encoding='utf-8') as fails:
            lasitajs = csv.reader(fails)
            for i in lasitajs:
                print(i)

    except FileNotFoundError:
        print("Fails netika atrasts.")

#lasit_csv()


#9. uzdevums

darbinieks = []

def pievienot(saraksts):
    try:
        with open('file.csv', 'a', encoding='utf-8') as fails:
            ID = input("Ievadiet personas ID numuru:")
            saraksts.append(ID)
            vards = input("Ievadiet personas vārdu:")
            saraksts.append(vards)
            vecums = input("Ievadiet personas vecumu:")
            saraksts.append(vecums)

            rakstitajs = csv.writer(fails)
            rakstitajs.writerow(saraksts)
    except FileNotFoundError:
        print("Fails netika atrasts.")

pievienot(darbinieks)