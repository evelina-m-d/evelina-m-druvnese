
class Skolotajs:
    def __init__ (self, vards, prieksmets):
        self.vards = vards
        self.prieksmets = prieksmets

    def iepazistinatArSevi(self):
        print(f"Sveiki, mani sauc {self.vards}!")
    def izliktVertejumu(self,punkti):
        if punkti>5:
            return f"Priekšmets {self.prieksmets} ir nokārtots!"
        else:
            return f"Priekšmets {self.prieksmets} nav nokārtots."


rinalds = Skolotajs("Rinalds", "Ģeogrāfija")
sandra=Skolotajs("Sandra", "Matemātika")

rinalds.iepazistinatArSevi()
print(rinalds.izliktVertejumu(8))
sandra.iepazistinatArSevi()
print(sandra.izliktVertejumu(4))