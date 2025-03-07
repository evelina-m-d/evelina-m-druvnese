
from abc import ABC, abstractmethod #importē palīgus abstraktajai klasei

class SkolasDarbinieks(ABC):
    def __init__(self, vards, uzvards, prieksmets=''): #kostruktors, kur obligāti objektam jābūt vārdam un uzvārdam, taču priekšmetu nav jāievada visiem darbiniekiem
        self.vards = vards
        self.uzvards = uzvards
        self.prieksmets = prieksmets

    @abstractmethod       #definē metodi kā abstraktu, lai tā būtu obligāti jāpārdefinē apakšklasēs
    def apraksts(self):
        pass

class Skolotajs(SkolasDarbinieks):   #skolotāja apakšklase, kas pieprasa priekšmetu
    def apraksts(self):
        return f"{self.vards} {self.uzvards} māca priekšmetu '{self.prieksmets}'."

class Dezurants(SkolasDarbinieks):    #dežuranta apakšklase, kas nepieprasa priekšmetu
    def apraksts(self):
        return f"{self.vards} {self.uzvards} saka, ka jāsavāc pazaudētās mantas no skolas pirmā stāva!"

class Saimnieks(SkolasDarbinieks):    #saimnieka apakšklase
    def apraksts(self):
        return f"{self.vards} {self.uzvards} labo salauzto loga eņģi."

darbinieki = [Skolotajs("Anda", "Lāce", "Audzināšana"), Dezurants("Jānis", "Straume"), Saimnieks("Johans", "Kalniņš")]      #saraksts ar skolas darbinieku objektiem un tiem atbilstošajiem datiem

for darbinieks in darbinieki:        #cikls kas, ejot cauri darbinieku sarakstam gan tos parāda konsolē, gan saglabā failā
    print(darbinieks.apraksts())
    with open('darbinieki.txt', 'a', encoding='utf-8') as fails:
        fails.write(f'{darbinieks.apraksts()}\n')