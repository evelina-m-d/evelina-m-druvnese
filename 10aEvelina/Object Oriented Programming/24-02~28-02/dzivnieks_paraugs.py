#definēt klasi dzivnieks, kas ir saistīta ar kāju skaitu
class Dzivnieks:
    def __init__(self,kaju_skaits=0): 
        self.kaju_skaits=kaju_skaits

    @classmethod #izmanto objektu izveidošanai ar noteiktu kāju skaitu
    def punts(kajas):
        return kajas(2) 
        
    @classmethod 
    def majlops(kajas):
        return kajas(4) 
    
    @classmethod 
    def simtkajis(kajas):
        return kajas(100) 
    
    #metode, kas izdrukā kāju skaitu
    def izdruka_kaju_skaitu(self):
        print(self.kaju_skaits)
    
#objekts(instance)
odze=Dzivnieks()
zoss=Dzivnieks.punts()
kaza=Dzivnieks.majlops()
simtkajis=Dzivnieks.simtkajis()


odze.izdruka_kaju_skaitu()
zoss.izdruka_kaju_skaitu()
kaza.izdruka_kaju_skaitu()
simtkajis.izdruka_kaju_skaitu()