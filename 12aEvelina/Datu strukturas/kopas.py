
klubsA={"Aldis", "Rolands", "Jēkabs", "Vadims", "Emīls","Igors"}
klubsB={"Vladislavs", "Vladimirs", "Rostislavs", "Vadims", "Igors"}
klubsC={"Ausma", "Jēkabs", "Emīls", "Austra", "Reičella", "Vadims"}

visi_klubi=klubsA.intersection(klubsB, klubsC)
print("Dalībnieki, kas piedalās visos klubos: ",*visi_klubi)

temp=klubsA.copy()
temp.intersection_update(klubsB)
print("A un B kopīgie dalībnieki: ", temp)

visi=klubsA.union(klubsB,klubsC)
print("Visi dalībnieki: ", visi)

klubsA.add("Jolanta")
print("A komanda: ", klubsA)

#klubsC.discard("Jēkabs")
print("C komanda: ", klubsC)

a = klubsA.difference(klubsB,klubsC)
print("Ir A, bet nav B vai C: ", a)

islaicigs = klubsA.copy()
islaicigs.difference_update(klubsB,klubsC)
print("Izņem visu no A, kas ir B un C: ", islaicigs)

