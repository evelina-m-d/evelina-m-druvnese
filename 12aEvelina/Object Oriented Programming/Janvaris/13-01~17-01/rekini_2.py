
import csv
import datetime

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
        merijumi = [int(i) for i in izmers.split()] 

        izmeri = f"{self.merijumi[-3]}cm x {self.merijumi[-2]}cm x {self.merijumi[-1]}cm"

        darba_samaksa = 15
        PVN = 21
        produkta_cena = velt_garums * 1.2 + (merijumi[0]/100 * merijumi[1]/100 * merijumi[2]/100) / 3 * materials 
        PVN_summa = (produkta_cena + darba_samaksa) * PVN/100
        rekina_summa = produkta_cena + darba_samaksa + PVN_summa

        return produkta_cena, PVN_summa, rekina_summa, izmeri

    def saglabat(self, klients, veltijums, izmers, materials):
        self.klients = klients
        self.veltijums = veltijums
        self.izmers = izmers
        self.materials = materials

        saglabajamais = []
        saglabajamais.append([self.klients, self.veltijums, izmeri, self.materials, rekina_summa])

        with open('kastites.csv', 'a', encoding='utf-8', newline='') as fails:
            writer = csv.writer(fails)
            writer.writerows(saglabajamais)
        
