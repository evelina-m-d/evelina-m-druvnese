
import csv

#1. uzdevums

saraksts = []

def pilsetas(saraksts):
    try:
        with open('pilsetas.csv', 'a', encoding='utf-8') as fails:
            for i in range(1,6):
                nosaukums = input(f"Ievadiet {i}. pilsētas nosaukumu:")
                saraksts.append(nosaukums)
                skaits = input(f"Ievadiet {i}. pilsētas iedzīvotāju skaitu:") 
                saraksts.append(skaits)
                rakstitajs = csv.writer(fails)
                rakstitajs.writerow(saraksts) #ievieto datus sarakstā un pievieno failam
                saraksts.clear()  #iztīra sarakstu nākamajai ievadei
    except FileNotFoundError:
        print("Fails netika atrasts.")

#pilsetas(saraksts)   #izkomentēts, lai neizsauktos visu funkciju testēšanas laikā


#2. uzdevums

def lasit_pilsetas():
    try:
        with open('pilsetas.csv', 'r', encoding='utf-8') as fails:
            lasitajs = csv.reader(fails)
            for i in lasitajs:
                for vards in i: #katra rindiņa ir savs saraksts, un otrais for cikls iet cauri katram mazajam sarakstam, kurā ir tikai pilsētas un iedzīvotāju skaits
                    print(vards)
                    print("-----------------------")

    except FileNotFoundError:
        print("Fails netika atrasts.")

#lasit_pilsetas()  #izkomentēts, lai neizsauktos visu funkciju testēšanas laikā


