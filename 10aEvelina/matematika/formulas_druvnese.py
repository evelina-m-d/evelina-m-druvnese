import math        
import random
rlRadius = int(input('Ievadiet riņķa līnijas rādiusu:\n'))   #Vieta, kur ievadīt rādiusa garumu
print(float(rlRadius))
PI = (math.pi)
rlGar = (rlRadius*PI*2)                    #Formulas, lai kalkulators spētu vispār strādāt
radKva = (math.pow(rlRadius,2))
rlLau = (PI*radKva)


print('Riņķa līnijas garums:' "%.2f"%rlGar) #Tiek parādīts rezultāts ar apaļošanu 2 skaitļus aiz komata
print('Riņķa līnijas laukums:' "%.2f"%rlLau)

pirmKat = int(input('Ievadiet taisnleņķa trijstūra pirmās katetes garumu:\n'))
otrKat = int(input('Ievadiet taisnleņķa trijstūra otrās katetes garumu:\n'))        #Vieta, kur ievadīt pirmo un otro katetes garumu
pirmKatKva = (math.pow(pirmKat,2))
otrKatKva = (math.pow(otrKat,2))                           #Vēl citas formulas, šoreiz trijstūrim
katSum = (pirmKatKva+otrKatKva)
trijHip = (math.sqrt(katSum))

print('Taisnleņķa trijstūra hipotenūzas garums:',"%.2f"%trijHip)   #Parāda hipotenūzas garumu ar apaļošanu 2 skaitļus aiz komata
radSka = random.random()
print('Gadījuma skaitlis no 0 - 1:',radSka)         #Tiek dots random skaitlis no 0 - 1
