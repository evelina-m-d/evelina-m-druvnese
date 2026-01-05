
#1. uzdevums
class Kubs: 
    def __init__(self, malas_garums=int, krasa=str):
        #malas garums var but no 2-10, ja neatbilst, tad uzstādīt default 2
        if malas_garums>=2 and malas_garums<=10:
            self.malas_garums = malas_garums
        else:
            print("Malas garums neatbilst nosacījumiem!") #paziņojums lietotājam
            self.malas_garums = 2
        self.krasa = krasa

    def aprekinat_tilpumu(self):
        tilpums = self.malas_garums * self.malas_garums * self.malas_garums #aprēķina tilpumu
        return tilpums

#1.2
kubg = Kubs(10, "zaļš")  #objekts, kam viss atbilst standartiem
#1.4, 1.5
print(f"Dati par kubg objektu: \nKubg krāsa un tilpums: {kubg.krasa}, {kubg.aprekinat_tilpumu()} cm^3 \nKubg malas garums: {kubg.malas_garums} cm")
print("***")

#1.3 
print("Dati par kubr objektu:") #objekts ar neatbilstošu malu garumu
kubr = Kubs(1, "sarkans")
#1.6, 1.7
print(f"Kubr krāsa un tilpums: {kubr.krasa}, {kubr.aprekinat_tilpumu()} cm^3 \nKubr malas garums: {kubr.malas_garums} cm")
print("***")

#2. uzdevums
class Bloks(Kubs):
    #2.1
    def __init__(self, malas_garums=int, krasa=str, kubu_skaits=int, forma=str, nosaukums=str, derigums=0):
        
        super().__init__(malas_garums, krasa)
        #kubu skaits var but no 1 līdz 4, ja neatbilst, tad uzstādīt default 1
        if kubu_skaits>=1 and kubu_skaits<=4:
            self.kubu_skaits = kubu_skaits
        else:
            #2.1.1
            print("Nepareiza kubu skaita vērtība!") #paziņojums lietotājam
            self.kubu_skaits = 1

        self.derigums = derigums
        self.forma = forma
        self.nosaukums = self.krasa + str(self.kubu_skaits)

        #forma var but no 11 līdz 14 un 22, ja neatbilst, tad derīgums = 0
        if self.forma == "11" or self.forma == "12" or self.forma == "13" or self.forma == "14" or self.forma == "22":
            self.derigums = 1
        else:
            #2.1.2
            print("Forma neatbilst nosacījumiem!") #paziņojums lietotājam
            self.derigums = 0

    def aprekinat_tilpumu(self):
        tilpums_kubam = self.malas_garums * self.malas_garums * self.malas_garums #bloka tilpuma formulas
        tilpums_blokam = tilpums_kubam * self.kubu_skaits
        return tilpums_blokam

#2.2 
oranzs3 = Bloks(5, "oranža", 3, "13") #objekts, kam viss atbilst standartiem
#2.3
print(f"Oranžs objekts: \n{oranzs3.nosaukums}, {oranzs3.aprekinat_tilpumu()} cm^3, derīgs {oranzs3.derigums}")
print("***")

print("Zils objekts:")
#2.4
zils5 = Bloks(7, "zila", 5, "23") #objekts ar neatbilstošu formu un kubu skaitu
#2.5
print(f"{zils5.nosaukums}, nederīgs {zils5.derigums}")
print("***")

#2.6
print("Mainīta forma:")  #objektu pārdefinē ar citu formu
zils5 = Bloks(7, "zila", 5, "12")
print(f"{zils5.nosaukums}, {zils5.malas_garums} cm, derīgs {zils5.derigums}")
print("***")