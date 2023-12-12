vardnica={ #vārdnīcas izveide ar visiem augumiem
    'Anna':172,
   'Pēteris':185,
    'Jānis':164,
    'Katrīna':184,
    'Līva':162,
    'Ralfs':164,
    'Artis':165,
    'Gatis':167,
    'Antra':177,
    'Marta':184,
    'Gustavs':165,
   'Amēlija':180
}

print('*********AUGUMU SARAKSTS*********')

for vards, augums in vardnica.items(): #stabiņa izprintē visus augumus un atbilstošos vārdus
    print(f'{vards:<10}:{augums}')

while True:
    darbiba=input('Vai vēlaties izdzēst vai pievienot datus, vai aprēķināt vidējo augumu? (izdzēst=i,pievienot=p,aprēķināt vidējo=a,redzēt jaunāko sarakstu=r,apstādināt programmu=stop)') #lietotājs izvēlas, ko vēlas darīt
    if darbiba=='i':
        izdzest=input('Kura skolēna garumu vēlaties izdzēst:') #lietotājs ievada vēlamo vērtību
        vardnica.pop(izdzest)
        print('Izdzēsāt',izdzest,'augumu.')
    elif darbiba=='p':
        pievienot=input('Kura skolēna garumu vēlaties pievienot:')
        garums=int(input('Kāds ir skolēna garums:'))
        vardnica[pievienot]=garums
        print('Pievienojāt',vards,'augumu')
    elif darbiba=='r':
        print('*****NESENĀKAIS AUGUMU SARAKSTS*****')
        for vards, augums in vardnica.items():
            print(f'{vards:<10}:{augums}')
    elif darbiba=='a':
        videjais = sum(vardnica.values()) / len(vardnica)
        print('*************\nVisu augumu vidējais ir:',videjais,'\n*************')
    else:
        break


    