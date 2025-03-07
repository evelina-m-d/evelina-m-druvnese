
#A uzdevums - bāzes klases izveide
class Masina:
    def __init__(self, marka, modelis, gads): #definē parametrus
        self.marka = marka
        self.modelis = modelis
        self.gads = gads

    #B uzdevums - metožu izveide
    def uzsakt(self):
        print(f"{self.marka} {self.modelis} sāk darboties.") #ziņojums par mašīnas darbības uzsākšanu, ar konkrētiem laukiem

    def apstaties(self):
        print(f"{self.marka} {self.modelis} ir apstādināta.")  #ziņojums par mašīnas darbības beigšanu, ar konkrētiem laukiem
    
    def info_par_auto(self):
        print(f"Marka: {self.marka}, Modelis: {self.modelis}, Gads: {self.gads}") #ziņojums, kas glīti izprintē mašīnas datus

#C uzdevums - pirmā objekta izveide, tā metožu izsaukšana
volvo1 = Masina("Volvo", "V60", 2007) #izveidots objekts ar konkrētiem atribūtiem
volvo1.info_par_auto() 
volvo1.uzsakt()            #izsauktas visas pieejamās metodes klasei
volvo1.apstaties() 

#D uzdevums - pirmās bērna klases izveide
class Elektro_Auto(Masina):
    def __init__(self, marka, modelis, gads, akumulatora_ietilp): 
        super().__init__(marka, modelis, gads)              #pārdefinē parametrus, pievieno jaunu
        self.akumulatora_ietilp = akumulatora_ietilp

#E, F uzdevums -  akumulatora procentu iestatīšana un baterijas pārbaudes metodes izveide
    def uzsakt(self, uzlades_limenis=100):
        if int(uzlades_limenis) > 20:                  #ja uzlādes līmenis zemāks nekā nepieciešams, ziņo lietotājam
            print(f"{self.marka} {self.modelis} sāk darboties. Akumulators: {uzlades_limenis}%") #ziņojums par mašīnas darbības uzsākšanu, ar konkrētiem laukiem, informē lietotāju, ja akumulatorā nav pietiekama baterija
        else:
            print(f"{self.marka} {self.modelis} nevar sākt darboties, jo akumulators pārāk zems: {uzlades_limenis}%.")

    def apstaties(self):
        return super().apstaties() #manto visu vecākklases metodi, bez izmaiņām

    #G uzdevums - funkcija izvada arī akumulatora ietilpību
    def info_par_auto(self):
        print(f"\nMarka: {self.marka}, Modelis: {self.modelis}, Gads: {self.gads} \nAkumulators: {self.akumulatora_ietilp} kWh") #ziņojums, kas glīti izprintē mašīnas datus, ieskaitot jauno atribūtu


#H uzdevums - otrā objekta izveide, tā metožu izsaukšana
tesla1 = Elektro_Auto("Tesla", "Cybertruck", 2020, 75)
tesla1.info_par_auto()
tesla1.uzsakt()

#I uzdevums - nepietiekama akumulatora simulēšana
tesla1.uzsakt(15)

#J uzdevums - otrās bērna klases izveide
class Degvielas_Auto(Masina):
    def __init__(self, marka, modelis, gads, bakas_tilpums): 
        super().__init__(marka, modelis, gads)              #pārdefinē parametrus, pievieno jaunu
        self.bakas_tilpums = bakas_tilpums

#K, L uzdevums -  degvielas tvertnes iestatīšana un tās pārbaudes metodes izveide
    def uzsakt(self, bakas_limenis=100): 
        if int(bakas_limenis) > 10:                   #ja bākas līmenis zemāks nekā nepieciešams, ziņo lietotājam
            print(f"{self.marka} {self.modelis} sāk darboties. Degvielas līmenis: {bakas_limenis}%") #ziņojums par mašīnas darbības uzsākšanu, ar konkrētiem laukiem 
        else:
            print(f"{self.marka} {self.modelis} nevar sākt darboties, jo degvielas līmenis pārāk zems: {bakas_limenis}%.") #informē lietotāju, ja bākā nav pietiekami degvielas

    def apstaties(self):
        return super().apstaties() #manto visu vecākklases metodi, bez izmaiņām

    #M uzdevums - funkcija izvada arī bākas tilpumu
    def info_par_auto(self):
        print(f"\nMarka: {self.marka}, Modelis: {self.modelis}, Gads: {self.gads} \nBākas tilpums: {self.bakas_tilpums} litri") #ziņojums, kas glīti izprintē mašīnas datus, ieskaitot jauno atribūtu


#N uzdevums - trešā objekta izveide, tā metožu izsaukšana
audi1 = Degvielas_Auto("Audi", "A7", 2022, 85)
audi1.info_par_auto()
audi1.uzsakt()

#O uzdevums = nepietiekama degvielas daudzuma simulēšana
audi1.uzsakt(5)