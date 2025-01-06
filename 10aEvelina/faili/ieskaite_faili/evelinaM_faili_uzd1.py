
#1. uzdevums

def pilsetas():
    with open('pilsetas.txt', 'w', encoding='utf-8', newline='') as fails:
        reizu_skaits = 1
        while reizu_skaits < 11:   #ļauj ievadīt tikai 10 reizes
            ieraksts = (input(f'Ievadiet pilsētu nr. {reizu_skaits}:') + '\n')
            ir_teksts = len(ieraksts) 
            if ir_teksts == 1:  #pārbauda, vai ievadītais ir tukša vieta 
                print('nevar būt tukša pilsēta!')
            else:
                fails.write(ieraksts)
                reizu_skaits += 1
        
    print("Pilsētas saglabātas!")

#pilsetas() #izkomentēts, lai neizsauktos visu funkciju testēšanas laikā


#2. uzdevums

def lasit_failu():
    try:
        with open('nolasit.txt', 'r', encoding='utf-8') as fails:
            vardi = fails.readlines()
            print("Teksts failā:")
            for ieraksts in vardi:
                    print(ieraksts.strip()) #sadala datus glīti, rindās
                    print("---------------------------")
    except FileNotFoundError:
        print("Fails nepastāv!")

#lasit_failu()  #izkomentēts, lai neizsauktos visu funkciju testēšanas laikā


#3. uzdevums

def kartotas_pilsetas():
    try:
        with open('pilsetas.txt', 'r', encoding='utf-8') as fails:
            pilsetas = []     #tukšs saraksts, kur tiks ievietoti pilsētu nosaukumi
            nosaukumi = fails.readlines()
            print("Pilsētas, sašķirotas alfabēta secībā:")
            for ieraksts in nosaukumi:
                smukas_pilsetas = ieraksts.strip()
                pilsetas.append((smukas_pilsetas))  #ievieto tukšajā sarakstā
            smuks_saraksts = sorted(pilsetas) #šķiro pilsētas pēc alfabēta
            for pilseta in smuks_saraksts: 
                print(pilseta)  #parāda konsolē
    except FileNotFoundError:
        print("Fails nepastāv!")


#kartotas_pilsetas()  #izkomentēts, lai neizsauktos visu funkciju testēšanas laikā


#4. uzdevums

def pievienot():
    with open('pilsetas.txt', 'a', encoding='utf-8', newline='') as fails:
        jaunaspilsetas = []
        reizu_skaits = 1
        while reizu_skaits < 4:   #atļauj tikai 3 reizes ievadīt
            ieraksts = (input(f'Ievadiet pilsētu nr. {reizu_skaits}:') + '\n')
            ir_teksts = len(ieraksts)
            
            if ir_teksts == 1:
                print('Nevar būt tukša pilsēta!')
            else:
                jaunaspilsetas.append(ieraksts) #pievieno sarakstu ar jaunajiem ierakstiem failam
                fails.write(ieraksts)
                reizu_skaits += 1    
    print("Šādas pilsētas saglabātas:")
    for i in jaunaspilsetas:
        print(i.strip())

#pievienot()  #izkomentēts, lai neizsauktos visu funkciju testēšanas laikā


