import datetime
import json

class Detala():  #satur tikai datus par detaļām, bez metodēm
    def __init__(self, nosaukums, marka, modelis, detalas_cena):
        self.nosaukums = nosaukums   
        self.marka = marka
        self.modelis = modelis
        self.detalas_cena = detalas_cena

class Piegadatajs(): #satur datus par piegadatajiem
    def __init__(self, laiks, min_apjoms, max_apjoms, cena_par_piegadi):
        self.laiks = laiks
        self.min_apjoms = min_apjoms
        self.max_apjoms = max_apjoms
        self.cena_par_piegadi = cena_par_piegadi

piegadataji = [
    Piegadatajs(2, 1, 100, 10),
    Piegadatajs(3, 1, 2, 3),
    Piegadatajs(4, 1, 120, 12)
]

def pasutijums(piegadatajs, detala): #ļauj pasūtīt detaļas un ievieto datus par tām failā
    while True:
        #detala = Detala(None, None, None, None)

        detala.nosaukums = input("Ievadiet, kādu detaļu jums vajag pasūtīt: ")
        detala.marka = input("Ievadiet, kādas mašīnas markas detaļa vajadzīga: ")
        detala.modelis = input("Ievadiet, kāds ir mašīnas modelis: ")
        while True:
            try:
                detala.detalas_cena = float(input("Ievadiet, kāda ir šīs detaļas cena: "))
                break
            except ValueError:
                print("Ievadiet cenu kā skaitli!")

        while True:
            try:
                skaits = int(input("Ievadiet detaļu skaitu: "))
                break
            except ValueError:
                print("Ievadiet skaitu kā skaitli!")
        
        datums = datetime.datetime.now() + datetime.timedelta(days=piegadatajs.laiks)
        kopeja_cena = detala.detalas_cena * skaits + piegadatajs.cena_par_piegadi
        print(f"Kopējā detaļu cena: {kopeja_cena}")
        try:
            with open('pasutijumi.json', 'r', encoding='utf8') as file:
                pasutijumi = json.load(file)
            
            faila_detala = {
                "nosaukums" : detala.nosaukums,
                "marka" : detala.marka,
                "modelis" : detala.modelis,
                "cena" : detala.detalas_cena,
                "skaits" : skaits,
                "piegādes diena" : datums.isoformat()
            }

            pasutijumi.append(faila_detala)
            with open('pasutijumi.json', 'w', encoding="utf8") as f:
                json.dump(pasutijumi, f, ensure_ascii=False)
        except FileNotFoundError:
            print("Vēl nav veikti pasūtījumi!")
        
        if input("Vai vēlaties pievienot vēl detaļas (j/n)? ") == "n":
            break

def pieraksts(vards, uzvards, detala, marka, modelis): #ļauj pierakstīt klientus un ievieto datus par tiem failā
    datums = datetime.datetime.now()

    with open('pieraksti.txt', 'a', encoding="utf8") as f:
        f.write(f"\n***\nKlienta vārds: {vards.capitalize()} {uzvards.capitalize()}\nPieraksta veikšanas datums: {datums.strftime('%d/%m/%Y')}\nMašīnas marka: {marka.capitalize()}\nMašīnas modelis: {modelis}\nNepieciešamās detaļas: {detala}")

def noliktava():
    try:
        with open('pasutijumi.json', 'r', encoding='utf8') as file:
            pasutijumi = json.load(file)
        piegadatie_pasutijumi = []

        for pasutijums in pasutijumi:
            laiks = pasutijums['piegādes diena']
            piegades_diena = datetime.datetime.fromisoformat(laiks)

            if piegades_diena <= datetime.datetime.now():
                pasutijums.pop("piegādes diena")
                piegadatie_pasutijumi.append(pasutijums)
                pasutijumi.remove(pasutijums)
            else:
                pass
        
        with open('pasutijumi.json', 'w', encoding='utf8') as file:
            json.dump(pasutijumi, file)
        with open('noliktava.json', 'w', encoding='utf8') as file:
            json.dump(piegadatie_pasutijumi, file)

    except FileNotFoundError:
        pass
    
    try:
        with open('noliktava.json', 'r') as file:
            preces = [json.loads(line) for line in file]

        print("Preces, kas atrodas noliktavā:")
        for i in preces:
            print(i)
    except FileNotFoundError:
        print("Noliktava ir tukša!")

    izvelne()

def izvelne():
    print("Servisa noliktavas un pierakstu uzskaites programma.")
    while True:
        izvele = input("****************************************************\n1-Apskatīt noliktavu\n2-Veikt klienta pierakstu\n3-Veikt pasūtījumu\n4-Iziet no programmas\nIzvēle: ")

        if izvele == "1":
            noliktava()
        if izvele == "2":
            vards = input("Kāds ir klienta vārds?:")
            uzvards = input("Kāds ir klienta uzvārds?:")
            marka = input("Kāda ir klienta mašīnas marka?: ")
            detala = input("Kādas detaļas klientam ir vajadzīgas? (atdalīt ar ', '): ")
            modelis = input("Kāds ir klienta mašīnas modelis?: ")
            pieraksts(vards, uzvards, detala, marka, modelis)
        if izvele == "3":
            piegadatajs = 0
            for i in piegadataji:
                print(f"Piegādātājs {piegadataji.index(i) +1} - pasūtījuma cena: {i.cena_par_piegadi}€, pasūtījuma laiks: {i.laiks} dienas, minimālais pasūtījuma daudzums: {i.min_apjoms}, maksimālais pasūtījuma daudzums: {i.max_apjoms}")
            while True:
                piegadatajs = int(input(f"Kādu piegādātāju jūs vēlaties (1 - {len(piegadataji)}): "))
                if piegadatajs < 1 or piegadatajs > len(piegadataji) +1:
                    print("Nepareizi ievadīts skaitlis!")
                else:
                    break

            pasutijums(piegadataji[int(piegadatajs)-1], Detala(None, None, None, None))
        if izvele == "4":
            print("Visu labu!")
            break

izvelne()