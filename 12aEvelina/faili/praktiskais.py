def parbaudit_vardu(vards):
    if not vards.isalpha():
        print("Vārdā drīkst būt tikai burti (bez cipariem vai simboliem).")# Pārbauda, vai vārds satur tikai burtus un nav tukšs.
        return False #atgriešanas vērtība(ja nebūs, tad atgriezīs None)
    #funkcija secināja, ka ievade ir nepareiza.Atgriež informāciju tai daļai, kur to izsauc,lai var apstrādāt(kā apstrādā?)
    return True #atgriešanas vērtība, ja ievade ir patiesa-vārds ir derīgs


def parbaudit_vecumu(vecums):
    if not vecums.isdigit():
        print("Vecumam jābūt skaitlim.")
        return False
    if int(vecums) <= 0:
        print("Vecumam jābūt lielākam par 0.")
        return False
    return True #Pārbauda, vai vārds satur tikai burtus un nav tukšs.


def normalizet_vardu(vards):
    return vards.strip().capitalize()

def vai_dublikats(vards, uzvards, vecums, faila_nosaukums):
    try:
        with open(faila_nosaukums, "r", encoding="utf8") as file:
            dati = file.readlines()
        ieraksts = f"{vards},{uzvards},{vecums}\n"
        return ieraksts in dati
    except FileNotFoundError:
        return False  # Fails vēl nav izveidots, tātad dublikātu nav.

def pievienot_datus_failam(faila_nosaukums):
    try:
        with open(faila_nosaukums, "a", encoding="utf8") as file:
            while True:
                vards = input("Ievadiet vārdu: ")
                if parbaudit_vardu(vards):
                    vards = normalizet_vardu(vards)
                    break
            while True:
                uzvards = input("Ievadiet uzvārdu: ")
                if parbaudit_vardu(uzvards):
                    uzvards = normalizet_vardu(uzvards)
                    break
            while True:
                vecums = input("Ievadiet vecumu: ")
                if parbaudit_vecumu(vecums):
                    break
            
            if vai_dublikats(vards, uzvards, vecums, faila_nosaukums):
                print("Šis ieraksts jau pastāv. Dati netika pievienoti.")
                return
            
            file.write(f"{vards},{uzvards},{vecums}\n")
            print("Dati pievienoti.")
    except Exception as e:
        print(f"Kļūda, saglabājot datus failā: {e}")

def paradit_datus(faila_nosaukums):
    try:
        with open(faila_nosaukums, "r", encoding="utf8") as file:
            dati = file.readlines()
        if not dati:  # pārbauda vai failā ir dati
            print("Fails ir tukšs. Pievienojiet datus.")
        else:
            print("\nDati no faila:")
            for ieraksts in dati:
                print(ieraksts.strip())
    except FileNotFoundError:
        print(f"Fails {faila_nosaukums} nepastāv!")

def iegut_vecumu_no_datiem(ieraksts):
    try:
        vecums = int(ieraksts.strip().split(",")[-1])
        return vecums
    except (IndexError, ValueError):
        return 0

def sakartot_un_paradit(faila_nosaukums):
    try:
        with open(faila_nosaukums, "r", encoding="utf8") as file:
            dati = file.readlines()
        if not dati:  # pārbauda vai failā ir dati
            print("Fails ir tukšs. Pievienojiet datus.")
        else:
            sakartoti_dati = sorted(dati, key=iegut_vecumu_no_datiem)  # kārto pēc funkcijas
            print('\nPēc vecuma sakārtoti dati:')
            for ieraksts in sakartoti_dati:
                print(ieraksts.strip())
    except FileNotFoundError:
        print(f"Fails {faila_nosaukums} nepastāv!")

# Programmas galvenā daļa
def izvelne():
    faila_nosaukums = "dati.txt"
    
    while True: 
        print("\nIzvēlieties opciju:")
        print("1 - Pievienot datus")
        print("2 - Parādīt datus")
        print("3 - Parādīt sakārtotus datus pēc vecuma")
        print("4 - Iziet")

        izvele = input("Izvēle: ")
        if izvele == "1":
            pievienot_datus_failam(faila_nosaukums)
        elif izvele == "2":
            paradit_datus(faila_nosaukums) 
        elif izvele == "3":
            sakartot_un_paradit(faila_nosaukums)    
        elif izvele == "4":
            print("Izvade tiek pārtraukta.")
            break    
        else:
            print("Nepareiza izvēle. Lūdzu, mēģiniet vēlreiz.")
            
izvelne()
