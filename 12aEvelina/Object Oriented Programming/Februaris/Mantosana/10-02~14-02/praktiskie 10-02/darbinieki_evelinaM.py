
class Darbinieks:
    def __init__(self, vards, uzvards, alga):
        self.vards = vards
        self.uzvards = uzvards
        self.alga = alga

    def uzraditInformaciju(self):
        print(f"Darbinieka vārds: {self.vards} {self.uzvards} \nDarbinieka alga: {self.alga}")

class Programmetajs(Darbinieks):
    def __init__(self, vards, uzvards, alga, ProgrammesanasVal):
        super().__init__(vards, uzvards, alga)
        self.ProgrammesanasVal = ProgrammesanasVal

    def uzraditInformaciju(self):
        print(f"Darbinieka vārds: {self.vards} {self.uzvards} \nDarbinieka mīļākā programmēšanas valoda: {self.ProgrammesanasVal} \nDarbinieka alga: {self.alga}")

class Pardevejs(Darbinieks):
    def __init__(self, vards, uzvards, alga, joma):
        super().__init__(vards, uzvards, alga)
        self.joma = joma

    def uzraditInformaciju(self):
        print(f"Darbinieka vārds: {self.vards} {self.uzvards} \nDarbinieka darba joma (ko pārdod): {self.joma} \nDarbinieka alga: {self.alga}")

class Vaditajs(Darbinieks):
    def __init__(self, vards, uzvards, alga, vaditajaAlga):
        super().__init__(vards, uzvards, alga)
        self.vaditajaAlga = vaditajaAlga

    def uzraditInformaciju(self):
        print(f"Vadītāja vārds: {self.vards} {self.uzvards} \nVadītāja alga: {self.vaditajaAlga}")


programmetajs = Programmetajs("Anna", "Puķīte", 4000, "Python")
programmetajs.uzraditInformaciju()

pardevejs = Pardevejs("Jānis", "Bērziņš", 1000, "Būvprodukti")
pardevejs.uzraditInformaciju()

vaditajs = Vaditajs("Elza", "Krastiņa", 7000, 7000)
vaditajs.uzraditInformaciju()
   
