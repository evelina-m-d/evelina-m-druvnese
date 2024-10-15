
import time

laiki = []
pieturas = []
cenas = []
kopejais_laiks = 0
kopeja_nauda = 0
nauda_uz_cilveku = 0
skaits = 0
klase = 0
cena = 0
pieturu_skaits = 0


def datu_ievade_ej():
    global cenas
    global laiki
    while True:
        try:
            attalums = float(input("Cik tālu iesiet? (km):"))
            if attalums < 1:
                raise ValueError
            else:
                break
        except ValueError:
            print("Ievadiet attālumu kā veselu, pozitīvu skaitli!")
            
    laiks = attalums/5
    laiki.append(laiks)

def datu_ievade_brauc():
    global laiki
    global cenas
    global cena

    while True:
        try:
            laiks = int(input("Cik ilgi brauksiet? (minūtēs):"))
            if laiks < 1:
                raise ValueError
            else:
                break
        except ValueError:
            print("Ievadiet minūtes pavadītas ceļā kā veselu, pozitīvu skaitli!")

    laiks2 = laiks/60
    laiki.append(laiks2)
        
    while True:
        try:
            cena = float(input("Cik maksā biļete vienam cilvēkam? (€):"))
            if cena < 1:
                raise ValueError
            else:
                break
        except ValueError:
            print("Ievadiet biļetes cenu kā pozitīvu skaitli!")

    cenas.append(cena)


def transporta_ievade():
    while True:
        try:
            transports = (input("Ar kādu transportu dosieties uz šo pieturu? (kājas/vilciens/autobuss):"))
            if transports == "kājas":
                datu_ievade_ej()
                break
            elif transports == "vilciens" or transports == "autobuss":
                datu_ievade_brauc()
                break
            else:
                raise IndexError
        except IndexError:
            print("Ievadiet kādu no pieejamajiem transportiem!")

def aprekins():
    global skaits
    global laiki
    global pieturas
    global cenas
    global kopeja_nauda
    global kopejais_laiks
    global nauda_uz_cilveku 

    kopejais_laiks = round(sum(laiki), 2) 
    kopeja_nauda = sum(cenas)*skaits
    nauda_uz_cilveku = round(kopeja_nauda/skaits, 2)

def beigas():
    print("Programma beidzas.")
    time.sleep(0.5)
    print("Programma beidzas..")
    time.sleep(0.5) 
    print("Programma beidzas...")
    time.sleep(0.8)
    print("Programma beigusies. Paldies! 👋")
    quit() 


def pieturu_ievade():
    global pieturu_skaits
    global skaits
    global pieturas

    while True:
        try:
            pieturu_skaits = int(input("Cik pieturas jūs veiksiet?:"))
            if pieturu_skaits < 1:
                raise ValueError
            else:
                break
        except ValueError:
            print("Ievadiet pieturu skaitu kā pozitīvu, veselu skaitli!")

    while True:
        try:
            skaits = int(input("Cik dalībnieku piedalās ekskursijā?:"))
            if skaits < 1:
                raise ValueError
            else:
                break
        except ValueError:
            print("Ievadiet dalībnieku skaitu kā pozitīvu, veselu skaitli!")

    for i in range(1, pieturu_skaits+1):
        nosaukums = input(f"Kāds ir {i}. pieturas nosaukums?:")
        pieturas.append(nosaukums)
        transporta_ievade()
    aprekins()

def atkartot():
    global cenas
    global laiki
    global pieturas
    global klase
    global kopeja_nauda
    global kopejais_laiks
    global nauda_uz_cilveku
    global pieturu_skaits 
    global pieturas

    x = True

    print("⋆ ˚｡⋆୨୧˚ Šī ir klases ekskursijas programma, kas palīdz analizēt cenas un laiku.˚୨୧⋆｡˚ ⋆")
    while True:
        print("************************************************************")
        klase = input("Ievadiet klasi (piemēram 11.a):")
        pieturu_ievade()
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~\n{klase} KLASES EKSKURSIJA:\n\n✩ Ekskursijas laikā apciemosiet šādas pieturas:")

        for i in pieturas:
            print(f".ೃ ࿐ {i}")

        print(f"\n✩ Pieturu skaits: {pieturu_skaits} pieturas\n✩ Kopējais laiks, kas pavadīts ceļā: {kopejais_laiks}h\n✩ Kopēja cena par transportu: {kopeja_nauda}€\n✩ Cena par transportu vienam cilvēkam: {nauda_uz_cilveku}€\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
        while True:
            try:
                repeat = input("Vai vēlaties atkārtot ekskursijas ievadi? (j/n):")
                if repeat == "n":
                    beigas()
                    quit()
                elif repeat == "j":
                    cenas.clear()
                    laiki.clear()
                    pieturas.clear()
                    break
                else: 
                    raise ValueError
            except ValueError:
                print("Ievadiet j vai n!")


atkartot()