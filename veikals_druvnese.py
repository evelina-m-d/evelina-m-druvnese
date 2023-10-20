stop = '0'
ceks = 'Iepirkšanās čeks:'
summa_bez_atlaides = 0.0
kopsumma = 0.0 #galējā summa

while stop == '0':
    ceks

    precu_skaits = int(input('Ievadiet preču skaitu:'))
    if precu_skaits < 0:
        exit()
    produkts = input('Ievadiet preces nosaukumu:')
    produkta_cena = round(float(input('Ievadi cenu 1 gabalam:')),2) #formatē ar 2 sk aiz komata

    #atlaides var izvēlēties, ierakstot skaitli no 1-5
    print('\n1-Maxima: 30% atlaide\n2-Elvi: 40% ar klienta karti\n3-Rimi: 20%, bet 50% ar klienta karti\n4-Mego: 30%, ja pērk 3 un vairāk preces\n5-Aibe: Katra otrā prece par brīvu')

    atlaides_veids = input('Izvēlēties veikalu (rakstiet ciparu no 1-5):')

    cena_bez_atlaides = produkta_cena*precu_skaits #iegūst cenu bez atlaidēm
    pirkuma_cena = cena_bez_atlaides #no pirkuma cenas rēķinās atlaides

    #sākas atlaižu aprēķins
    if atlaides_veids == '1': #atlaide maximā
        #pirkuma_cena = pirkuma_cena*0.7
        pirkuma_cena*=0.7  #izmanto salikto operatoru
    
    elif atlaides_veids == '2': #atlaide elvi
        atl_karte = input('Vai jums ir klienta karte?:')
        if atl_karte == 'j':
            pirkuma_cena*=0.6
        elif atl_karte == 'n':
            pirkuma_cena = pirkuma_cena
    
    elif atlaides_veids == '3': #atlaide rimi
        atl_karte_rimi = input('Vai jums ir atlaižu karte?:')
        if atl_karte_rimi == 'j':
            pirkuma_cena*=0.5
        elif atl_karte_rimi == 'n':
            pirkuma_cena*=0.8
