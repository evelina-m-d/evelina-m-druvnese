import datetime


class Detala():  #satur tikai datus par detaļām, bez metodēm
    def __init__(self, nosaukums, marka, modelis, detalas_cena):
        self.nosaukums = nosaukums   
        self.marka = marka
        self.modelis = modelis
        self.detalas_cena = detalas_cena

class Skidrumi():  #satur tikai datus par šķidrumiem, bez metodēm
    def __init__(self, nosaukums, deriguma_termins, cena):
        self.nosaukums = nosaukums
        self.deriguma_termins = deriguma_termins #te vajag atrast veidu kaa pieskaitit pie datuma gadus klat  
        self.cena = cena

class Klients():  #satur datus par katra klienta pierakstu
    def __init__(self, nepieciesamas_detalas, marka, modelis):
        self.nepieciesamas_detalas = nepieciesamas_detalas
        self.pieraksta_laiks = datetime.now()
        self.marka = marka
        self.modelis = modelis

    def remontet(self, stundu_skaits): 
            stundas_likme = 50 #eiro
            cena = (stundu_skaits * stundas_likme) + self.nepieciesamas_detalas.detalas_cena #aprēķina izmaksas klientam
            return cena

            #butu janonem no noliktavas detala bet to izdomas kad bus kopa salikts

class Piegadatajs():
    def __init__(self, laiks, min_apjoms, max_apjoms, cena):
        self.laiks = laiks
        self.min_apjoms = min_apjoms
        self.max_apjoms = max_apjoms
        self.cena = cena
        