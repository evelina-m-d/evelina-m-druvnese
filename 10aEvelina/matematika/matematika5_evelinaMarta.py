print('Programmu izstrādāja: Evelīna Marta Druvnese.','\n','\nLaukuma aprēķins ģeometriskām figūrām','\n\t****') #Autora vārds

malaA = int(input('Ievadiet malas A garumu:\n'))  #Vieta, kur ievadīt malu un augstuma vērtības
print('Malas A garums:',float(malaA),'\n\t****')
malaB = int(input('Ievadiet B malas garumu:\n'))
print('Malas B garums:',float(malaB),'\n\t****')
high = int(input('Ievadiet augstumu:\n'))
print('Augstums:',float(high),'\n\t****')

triFormula = (malaA*high) /2    #Formulas, lai aprēķini varētu notikt
paraFormula = (malaA*high)
trapFormula1 = (malaA+malaB) /2
trapFormula2 = (trapFormula1*high)

print('Laukums trijstūrim:',triFormula)
print('Laukums trapecei:',trapFormula2)  #Tiek parādīti gala rezultāti
print('Laukums paralelogramam:', float(paraFormula),'\n\t****','\nPaldies!')