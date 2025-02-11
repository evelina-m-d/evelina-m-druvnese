
class Transportlidzeklis:
    def __init__(self, transports):
        self.transports = transports
    
    def parvietoties(self):
        print("Transports parvietojas! ദ്ദി(•ᴗ• )")

class Auto(Transportlidzeklis):
    def __init__(self, transports):
        super().__init__(transports)

    def parvietoties(self):
        print("Auto brauc pa ceļu! ō͡≡o")

class Lidmasina(Transportlidzeklis):
    def __init__(self, transports):
        super().__init__(transports)

    def parvietoties(self):
        print("Lidmašīna lido pa gaisu! ⋆｡ﾟ☁︎｡✈︎  ☾ ﾟ｡⋆")

class Velosipeds(Transportlidzeklis):
    def __init__(self, transports):
        super().__init__(transports)

    def parvietoties(self):
        print("Velosipēds brauc pa taku! 🚴‍♀️")

masina = Auto("masina")
lidmasina = Lidmasina("lidmasina")
ritenis = Velosipeds("ritenis")

Transporti = [masina, lidmasina, ritenis]

for i in Transporti:
    i.parvietoties()