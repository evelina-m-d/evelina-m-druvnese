import csv
from datetime import datetime

class Rekins:
    def __init__ (self, klients, veltijums, izmers, materials):
        self.klients = klients
        self.veltijums = veltijums
        self.izmers = izmers
        self.materials = materials
        
        self.laiks = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def aprekins(self, veltijums, izmers, materials):
        global rekina_summa
        global merijumi
        self.veltijums = veltijums
        self.izmers = izmers
        self.materials = materials

        velt_garums = len(veltijums)
        self.merijumi = [int(i) for i in izmers.split()] 

        darba_samaksa = 15
        PVN = 21
        produkta_cena = velt_garums * 1.2 + (merijumi[0]/100 * merijumi[1]/100 * merijumi[2]/100) / 3 * materials 
        PVN_summa = (produkta_cena + darba_samaksa) * PVN/100
        rekina_summa = produkta_cena + darba_samaksa + PVN_summa

    def izdruka(self, izmers, veltijums, materials):
        global rekina_summa 
        self.veltijums = veltijums
        self.izmers = izmers
        self.materials = materials

        velt_garums = len(veltijums)
        self.merijumi = [int(i) for i in izmers.split()] 

        darba_samaksa = 15
        PVN = 21
        produkta_cena = velt_garums * 1.2 + (self.merijumi[0]/100 * self.merijumi[1]/100 * self.merijumi[2]/100) / 3 * materials 
        PVN_summa = (produkta_cena + darba_samaksa) * PVN/100
        rekina_summa = produkta_cena + darba_samaksa + PVN_summa

        print("******************\nRĒĶINS\n******************") 
        print(f"Klients: {self.klients} \nVeltījums: {self.veltijums} \nIzmēri: {self.merijumi[-3]} x {self.merijumi[-2]} x {self.merijumi[-1]} \nMateriāla cena: {self.materials}€ \nApmaksas summa: {rekina_summa}€  \nRēķina izveides laiks: {self.laiks}")
        self.merijumi.clear()   


rekina_sakums = print("Labdien! Lūdzu ievadiet produkta datus.")
klients = input("Klienta vārds:") 
veltijums = input("Veltījums, ko vēlaties uz kastītes:")
izmers = input("Izmēri (trīs veseli skaitļi, atdalīti ar atstarpēm):")       
materials = float(input("Materiāla cena (€/cm3):"))

Kastite1 = Rekins(klients, veltijums, izmers, materials)

Kastite1.izdruka(izmers, veltijums, materials)