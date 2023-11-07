'''* izveidot 3 sarakstus: lietotājs pats norāda 
cik elementus likt sarakstā.
* pirma un otra saraksta vertibas ievada lietotajs
* tresa saraksta vertibas iegust apvienojot pirmos 2 
sarakstus
* katra saraksta saturu gliti paradit uz ekrana'''

saraksts = []
pirmsar = int(input('Ievadi pirmā saraksta elementu skaitu: '))
for i in range(0,pirmsar):
    elem = input('Ievadi elementus: ')
    saraksts.append(elem)

saraksts2 = []
otrsar = int(input('Ievadi otrā saraksta elementu skaitu: '))
for x in range(0,otrsar):
    elem2 = input('Ievadi elementus: ')
    saraksts2.append(elem2)

saraksts3 = saraksts + saraksts2
print('**************\nPirmais saraksts: ',saraksts)
print('Otrais saraksts: ',saraksts2)
print('**************\nKopējais saraksts ir: ',saraksts3,'\n**************')
