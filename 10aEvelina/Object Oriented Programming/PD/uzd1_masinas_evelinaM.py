
class Transportlidzeklis:   #definēta klase
    def __init__(self, zimols, modelis, reg_datums, pilna_masa, degvielas_veids):   #klasei pievienoti visi aktuālie parametri
        self.zimols = zimols
        self.modelis = modelis
        self.reg_datums = reg_datums
        self.pilna_masa = pilna_masa
        self.degvielas_veids = degvielas_veids

    def paradit(self):   #klasei definēta metode, kas glīti izvada aktuālos datus
        print("*****************************\nAUTOMAŠĪNAS DATI\n*****************************")
        print(f"Zīmols: {self.zimols} \nModelis: {self.modelis} \nReģistrācijas datums: {self.reg_datums} \nPilna masa: {self.pilna_masa}kg \nDegvielas veids: {self.degvielas_veids}" )

Masina1 = Transportlidzeklis("Audi", "A4", "22.10.2019.", "1800", "BG")   #izveidots objekts pēc dotajiem datiem
Masina1.paradit()   #izsaukta iepriekš definētā metode