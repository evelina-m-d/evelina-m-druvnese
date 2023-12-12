def kmi(masa,augums):
    indekss = round((masa/((augums/100)*(augums/100))),2)
    print("************\nJūsu ĶMI ir:",indekss,';')
    if indekss > 30:
        print('Aptaukošanās!')
    elif indekss < 18.5:
        print('Nepietiekama ķermeņa masa!')
    elif indekss > 18.5 and indekss < 24.99:
        print('Normāla ķermeņa masa!')
    elif indekss > 25 and indekss <29.99:
        print('Lieka ķermeņa masa!')
    print('************')

masa = float(input("Ievadi savu masu, kg:"))
augums = float(input('Ievadi savu augumu, cm:'))

kmi(masa,augums)
