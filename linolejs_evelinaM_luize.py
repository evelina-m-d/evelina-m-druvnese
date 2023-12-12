
import math #importē matemātiku

lin_izmaksas_kopa = 0  #šī brīža izmaksas

rekini = 'j'
while rekini == 'j': #kamēr reiķini irf jā, programma turpina jautāt
    lin_cena = int(input('Ievadiet linoleja cenu:'))                        #lietotājs piešķir vērtības
    rull_plat = int(input('Ievadiet linoleja ruļļa platumu (metros):'))      #''-----------------''
    telp_plat = int(input('Ievadiet telpas platību kvadrātmetros:'))          #''-----------------''
    apaks = input('Vai klients vēlas apakšklāju (jā=j, nē=n):')                 #''-----------------''
    
    cena_apaks = 0  #šī brīža cena apakšklājam
    if apaks == 'j': #apreiķini ja ir vajadzīgs apakšklājs
        cena_apaks = int(input('Ievadiet apakšklāja cenu:'))
    
    
    telpas_garums = math.sqrt(telp_plat) #aprēķina telpas sienas garumu(pieņemot ka telpa kvadrāts)
    telpas_garums = round(telpas_garums, 2) #noapaļo kvadrātsakni līdz diviem skaitļiem aiz komata
    lin_daudzums = telpas_garums / rull_plat #aprēķina linoleja daudzumu
    apaks_izmaksas = cena_apaks * lin_daudzums #aprēķina apakšklāja izmaksas
    lin_vienspats = lin_daudzums * lin_cena #aprēķina linoleja paša izmaksas
    lin_izmaksas = lin_vienspats + apaks_izmaksas #aprēķina kopējās linoleja izmaksas
 

    lin_izmaksas_kopa += lin_izmaksas
    

    print("**********************\nČEKS")
    print("Linoleja cena:", lin_vienspats, ' eiro\nApakšklāja cena:', apaks_izmaksas, ' eiro\nKopējā cena:', lin_izmaksas, ' eiro')
    print("**********************")
    
    rekini = input('Vai vēlaties rēķināt vel (jā=j, nē=n):')


print("Kopējās izmaksas visiem ievadītajiem linolejiem:", lin_izmaksas_kopa, ' eiro')
