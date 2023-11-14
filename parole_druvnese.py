#lietotājvārds ir Kakis123, parole 12345

print('Ievadi lietotājvārdu un paroli! (tev ir pieci mēģinājumi)\n') #pastāsta lietotājam ko darīt
count=0
while count <=4:
    username = input('Ievadi lietotāju: ') #paroles un lietotājvārda ievade
    password = input('Ievadi paroli: ')
    if password=='12345' and username=='Kakis123':
        print('Pareizi! (ievadi 0 lai izbeigtu programmu)') 
        onenumber = int(input('Ievadi pirmo veselo skaitli: ')) #pirmā skairtļa ievade
        if onenumber == 0:
                print('Programmas beigas.') #ja ievada 0 (stop vietā) tad programma beidzas
                break
        elif onenumber < 0:
             print('Nedrīkst rēķināt ar negatīvu skaitli!') #negatīva skaitļa ievad izmet kļūdu
             break
        else:
            twonumber = int(input('Ievadi otro veselo skaitli: '))  #viss tas pats kas ar pirmā skaitļa ievadi
            if twonumber == 0:
                 print('Programmas beigas.')
            elif twonumber < 0:
                 print('Nedrīkst rēķināt ar negatīvu skaitli!')
                 break
            elif twonumber > onenumber:
                 total = sum(range(onenumber, twonumber+1))
                 print('Veselu secīgi pieaugošu skaitļu no ',onenumber,' līdz ',twonumber,' summa ir ',total,'.') #skaitļu secībasd summas aprēķins tiek parādīts
                 break
    else:
        count += 1
        remaining = 5-count #skaita, cik reizes kļūdās paroles/lietotāja ievadē, pie piektās reizes neļauj vairs ievadīt
        if remaining == 0:
             print('Izmantotas visas piecas iespējas!')
             break
        else:
             print('Nepareizs lietotājvārds vai parole. Parolei jābūt 5 rakstzīmes garai! Atlikuši vēl ',remaining,' iespēja(s).') #dod lietotājam ziņu, cik reizes viņš vēl var ivadīt paroli/lietotāju
