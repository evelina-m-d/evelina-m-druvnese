paskaits = int(input('Cik būs pasažieru? (ievadi veselu skaitli):'))
if paskaits > 3:
    print('Par daudz pasažieru. taksi nevar izsaukt.')
elif paskaits > 0 and paskaits < 4:
    plkst = int(input('Cik šobrīd ir pulkstens? (ievadi veselu stundu):'))
    if int(plkst) in range(1, 24):
           stvta = (input('Vai pie stacijas stāv kāds taksis? (j/n):'))
           if stvta == 'j' or 'n':
                stlks = int(input('Cik minūtes šoferim būs jāgaida? Šoferis negaidīs ilgāk par pusstundu! (veselos skaitļos, ja nebūs, tad raksti 0):'))
                if stlks > 30:
                     print('Šoferis tik ilgi negaidīs! Mēģini vēlāk.')
                elif int(stlks) in range (0, 31):
                     att = int(input('Cik km brauksi? Šoferis nevedīs vairāk par 50km! (Pilnos km):'))
                     if int(att) in range (1, 51):
                          print('\t***************\n \tČeks: \n\tMaksa par takša pakalpojumu: 2,00 Eiro')

if int(plkst) in range (6, 20): 
    print('\tDienas tarifs: 0,37 Eiro par KM')
elif int(plkst) in range (21, 24) or int(plkst) in range (1, 5):
    print('\tNakts tarifs: 0,77 Eiro par KM')
if int(att) in range(1, 50):
    print('\t Nobrauktie KM:', att) 
if stlks > 0:
     print('\tTarifs par stāvēšanu: 0,15 Eiro/min')
if stlks > 0:
    stlkskop = stlks*0.15
    print('\t Nostāvētās minūtes:',stlks)
elif stlks == 0:
    print('\tŠoferis negaida.')
if int(plkst) in range (6, 20):
     tarifs = 0.37
elif int(plkst) in range (21, 24) or int(plkst) in range (1, 5):
    tarifs = 0.77
if stlks == 0:
     kopCenbstv = (tarifs*att)+2.0
else:
     kopCenbstv = (tarifs*att)+stlkskop+2.0
if stvta == 'n':
     print('\tIzsaukšanas tarifs: 2,50 Eiro')
if stvta == 'n': 
    kopCen = kopCenbstv + 2.50
elif stvta == 'j':
     kopCen = kopCenbstv 

print('\t','Kopējā cena:',kopCen,'Eiro\n\t***************')