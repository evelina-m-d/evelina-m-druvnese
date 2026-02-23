
darzeni = ["burkans", "kartupelis", "kaposts"]

def funkcija(saraksts):
    print(f"Saraksta garums: {len(saraksts)}\nSaraksta elementi:")
    for i in saraksts:
        print(f"{i}")
    print("-----------------------------------")

funkcija(darzeni)

darzeni.append("kalis")

funkcija(darzeni)

darzeni.pop(2)

funkcija(darzeni)

#----------------------------------------------------------------------------------------------

putni = ["Vārna", "Gulbis", "Flamingo"]
visgarakais = max(putni,key=len)
print("Visgarākais putna vārds: ", visgarakais, "\n-----------------------------------")

#---------------------------------------------------------------------------------------------

apvienots = darzeni + putni
print("Apvienots:", apvienots)