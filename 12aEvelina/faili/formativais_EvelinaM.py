
import time

vards_skaits = 0
vecums_skaits = 0 #mainīgie, kas nosaka, kad jānobeidz programma pie 3 vārda, atzīmes vai vecuma kļūdām
atzime_skaits = 0
 
def ir_vards(vards): #funkcija vārda satura pārbaudīšanai
    global vards_skaits 

    if vards == 'stop' or vards == 'STOP':
        print("Izvade tiek pārtraukta.")
        time.sleep(0.5)
        print("Izvade tiek pārtraukta..") #glīti izprintē programmas beigas
        time.sleep(0.5)
        print("Izvade tiek pārtraukta...")
        time.sleep(0.8)
        print("Programma Beigusies.")
        quit()

    if not vards.isalpha():
        print("Kļūda. Vārdā un uzvārdā drīkst būt tikai burti.")
        vards_skaits += 1
        if vards_skaits == 3:
            print("Ievadījāt nepareizi 3 reizes. Pārsniegts mēģinājumu skaits. Programma beidzas.") #beidz programmu pēc 3 kļūdām
            quit()
        return False    
    return True

def ir_vecums(vecums): #funkcija vecuma pārbaudīšanai
    global vecums_skaits

    if vecums == 'stop' or vecums == 'STOP':
        print("Izvade tiek pārtraukta.")
        time.sleep(0.5)
        print("Izvade tiek pārtraukta..") #glīti izprintē programmas beigas
        time.sleep(0.5)
        print("Izvade tiek pārtraukta...")
        time.sleep(0.8)
        print("Programma Beigusies.")
        quit()

    if not vecums.isdigit():
        print("Kļūda. Vecumam jābūt veselam skaitlim.")
        vecums_skaits += 1
        if vecums_skaits == 3:
            print("Ievadījāt nepareizi 3 reizes. Pārsniegts mēģinājumu skaits. Programma beidzas.") #beidz programmu pēc 3 kļūdām
            quit()
        return False
    if int(vecums) <= 0:
        print("Kļūda. Vecumam jābūt pozitīvam.")
        if vecums_skaits == 3:
            print("Ievadījāt nepareizi 3 reizes. Pārsniegts mēģinājumu skaits. Programma beidzas.")
            quit()
        vecums_skaits += 1
        return False
    return True 

def ir_atzime(atzime): #funkcija atzīmju pārbaudīšanai
    global atzime_skaits

    if atzime == 'stop' or atzime == 'STOP':
        print("Izvade tiek pārtraukta.")
        time.sleep(0.5)
        print("Izvade tiek pārtraukta..") #glīti izprintē programmas beigas
        time.sleep(0.5)
        print("Izvade tiek pārtraukta...")
        time.sleep(0.8)
        print("Programma Beigusies.")
        quit()

    if not atzime.isdigit():
        print("Kļūda. Atzīmei jābūt veselam skaitlim.")
        atzime_skaits += 1
        if atzime_skaits == 3: 
            print("Ievadījāt nepareizi 3 reizes. Pārsniegts mēģinājumu skaits. Programma beidzas.") #beidz programmu pēc 3 kļūdām
            quit()
        return False

    if int(atzime) < 0:
        print("Kļūda. Atzīmei jābūt pozitīvai vai 0.")
        atzime_skaits += 1
        if atzime_skaits == 3:
            print("Ievadījāt nepareizi 3 reizes. Pārsniegts mēģinājumu skaits. Programma beidzas.")
            quit()
        return False
    elif int(atzime) > 10:
        print("Kļūda. Atzīmei jābūt no 1 - 10.")
        atzime_skaits += 1
        if atzime_skaits == 3:
            print("Ievadījāt nepareizi 3 reizes. Pārsniegts mēģinājumu skaits. Programma beidzas.")
            quit()
        return False

    return True 

def noformets_vards_vai_uzvards(vards): #funkcija, kas uzraksta vārdu un uzvārdu ar lielo burtu
    return vards.strip().capitalize()

def ievade(faila_nosaukums): #funkcija kurā lietotājs ievada datus un tie tiek uzreiz pievienoti
    try:
        with open(faila_nosaukums, "a", encoding="utf8") as file:
            while True:
                vards = input("Ievadiet vārdu: ")
                if ir_vards(vards):
                    vards = noformets_vards_vai_uzvards(vards)
                    break
            while True:
                uzvards = input("Ievadiet uzvārdu: ")
                if ir_vards(uzvards):
                    uzvards = noformets_vards_vai_uzvards(uzvards)
                    break
            while True:
                vecums = input("Ievadiet vecumu: ")
                if ir_vecums(vecums):
                    break
            while True:
                atzime = input("Ievadiet atzīmi: ")
                if ir_atzime(atzime):
                    break
            
            file.write(f"{vards}   {uzvards}   {vecums}   {atzime}\n")
            print("Dati saglabāti failā: kontroldarbs.txt")
    except Exception as e:
        print(f"Kļūda, saglabājot datus failā: {e}")

def iegut_atzimi_no_datiem(ieraksts): #funkcija kas izloba atzīmi no faila
    try:
        atzime = int(ieraksts.strip().split("   ")[-1])
        return atzime
    except (IndexError, ValueError):
        return 0

def parada(faila_nosaukums): #funkcija kas sašķiro datus pēc atzīmēm un izprintē konsolē
    try:
        with open(faila_nosaukums, "r", encoding="utf8") as file:
            dati = file.readlines()
        if not dati:  #pārbauda, vai failā ir dati
            print("Nav datu, ko parādīt.")
        else:
            sakartoti_dati = sorted(dati, key=iegut_atzimi_no_datiem)  
            print('\nPēc atzīmes sakārtoti dati:\nVārds: Uzvārds: Vecums: Atzīme:')
            for ieraksts in sakartoti_dati:
                print(ieraksts.strip())
    except FileNotFoundError:
        print(f"Fails {faila_nosaukums} nepastāv!")

# Programmas lietotāja saskarsnes daļa

def izvelne():
    faila_nosaukums = "kontroldarbs.txt" 
        
    while True: 
        print("Kontroldarba atzīmju ievades programma.\n******************************************")
        print("\nIzvēlieties darbību:")
        print("1 - Ievadīt un saglabāt datus failā")
        print("2 - Parādīt sakārtotus datus pēc gala atzīmes (augošā secībā)")
        print("3 - Iziet")

        izvele = input("Jūsu izvēle: ")
        if izvele == "1":
            ievade(faila_nosaukums)
        elif izvele == "2":
            parada(faila_nosaukums)    
        elif izvele == "3":
            print("Izvade tiek pārtraukta.")
            time.sleep(0.5)
            print("Izvade tiek pārtraukta..") #glīti izprintē programmas beigas
            time.sleep(0.5)
            print("Izvade tiek pārtraukta...")
            time.sleep(0.8)
            print("Programma Beigusies.")
            break    
        else:
            print("Nepareiza izvēle. Lūdzu, mēģiniet vēlreiz.")

        while True:
            turpinat = input("Vai vēlaties turpināt ievadi? (j/n):") #prasa lietotājam, vai tas vēlas vēl veikt kādu darbību
            if turpinat == "n":
                print("Izvade tiek pārtraukta.")
                time.sleep(0.5)
                print("Izvade tiek pārtraukta..") #glīti izprintē programmas beigas
                time.sleep(0.5)
                print("Izvade tiek pārtraukta...")
                time.sleep(0.8)
                print("Programma Beigusies.")
                quit()
            elif turpinat == "j":
                break
            else:
                print("Ievadei jābūt j/n!") #kļūdas gadījumā ziņo lietotājam
                continue
            
izvelne()
