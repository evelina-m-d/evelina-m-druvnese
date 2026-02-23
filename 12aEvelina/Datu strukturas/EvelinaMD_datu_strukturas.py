
#darbs ar sarakstiem------------------------------------------------------------------------------------------

sporta_skoleni = ["Anna", "Jēkabs", "Santa", "Viktorija", "Daniels", "Emīlija", "Monika", "Kristaps", "Aleksis"]

print("***************************************************")
print("Sakārtots Sporta dienas dalībnieku saraksts:", sorted(sporta_skoleni))
print("Dalībnieku skaits:", len(sporta_skoleni))
print("Skolēns, kas atteicies piedalīties:", sporta_skoleni.pop(3))
print("Sporta dienas dalībnieku saraksts bez šī skolēna:", sorted(sporta_skoleni))

zinatnes_skoleni = ["Anna", "Jēkabs", "Jolanta", "Kaiva", "Rūdolfs", "Alise", "Kristers", "Varis"]

#darbs ar kortežiem------------------------------------------------------------------------------------------

skolas_pasakumi = [("Sporta diena", "Stadions", 120), ("Zinātnes diena", "Lielā zāle", 50), ("Karjeras diena", "307. kabinets", 24)]

print("***************************************************")
print("Visi pasākumi:")
for pasakums in skolas_pasakumi:
    print(f"Pasākums: {pasakums[0]} | Norises vieta: {pasakums[1]} | Maksimālais dalībnieku skaits: {pasakums[2]}")

#darbs ar kopām----------------------------------------------------------------------------------------------

sporta_diena = set(sporta_skoleni)
zinatnes_diena = set(zinatnes_skoleni)
sporta_diena.add("Veronika")
abi = sporta_diena.intersection(zinatnes_diena)
tikai_sp = sporta_diena.difference(zinatnes_diena)
visi = sporta_diena.union(zinatnes_diena)

print("***************************************************")
print("Pasākumam 'Sporta diena' tiek pievienots skolēns 'Veronika', Sporta dienas dalībnieku saraksts:", sporta_diena)
print("\nGan Sporta dienā, gan Zinātnes dienā piedalās:", abi)
print("\nSkolēni, kas piedalās tikai Sporta dienā:", tikai_sp)
print("\nVisi skolēni, kas piedalās vismaz vienā pasākumā:", visi)

#darbs ar vārdnīcu-------------------------------------------------------------------------------------------

skoleni_un_pasakumi = {
    "Anna": ["Sporta diena", "Zinātnes diena"],
    "Jēkabs": ["Sporta diena", "Zinātnes diena"],
    "Santa": ["Sporta diena"],
    "Viktorija": ["Sporta diena"],
    "Daniels": ["Sporta diena"],
    "Emīlija": ["Sporta diena"],
    "Monika": ["Sporta diena"],
    "Kristaps": ["Sporta diena"],
    "Aleksis": ["Sporta diena"],
    "Kaiva": ["Zinātnes diena"],
    "Jolanta": ["Zinātnes diena"],
    "Rūdolfs": ["Zinātnes diena"],
    "Alise": ["Zinātnes diena"],
    "Kristers": ["Zinātnes diena"],
    "Varis": ["Zinātnes diena"]
}

skoleni_un_pasakumi["Monika"].append("Zinātnes diena")
skoleni_un_pasakumi["Sanija"] = ["Sporta diena", "Zinātnes diena"]
