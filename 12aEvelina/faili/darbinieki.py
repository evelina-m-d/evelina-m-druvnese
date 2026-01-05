import csv

fails = "darbinieki.csv"

darbinieki = [
    {"Vārds":"Jānis", "Amats":"Inženieris", "Alga":"800"},
    {"Vārds":"Imants", "Amats":"Galdnieks", "Alga":"500"},
    {"Vārds":"Jānis", "Amats":"Inženieris", "Alga":"800"}
]

with open(fails, 'w', encoding='utf-8', newline='') as fails:
    w = csv.DictWriter(fails, darbinieki.keys())
    w.writeheader()
    w.writerow(darbinieki)

try:
    with open(fails, 'w', encoding='utf-8', newline='') as fails:
        reader=csv.DictReader(fails)
        algas_filtrs = []
        for rinda in reader:
            try:
                alga = int(rinda['Alga'])
                if alga > 1000:
                    algas_filtrs.append(rinda)
            except ValueError:
                print(f"Brīdinājums: Rindā {rinda['Vārds']} {rinda['Amats']} nav der\īga alga.")
except FileNotFoundError:
    print(f'Fails "{fails}" nav atrasts!')
except Exception as e:
    print(f'Kļūda nolasot failu: {e}')