
class Viesis:
    def __init__(self, vards, parole):
        self.vards = vards
        self.parole = parole

    def druka_vardu(self):
        print(f"Lietotājs {self.vards} ir izveidots")

    def parbauda_paroli(self,parole):
        if self.parole == parole:
            print(f"Lietotāja {self.vards} parole ir pareiza!")

        else:
            print("Parole nav pareiza!")

class Darbinieks(Viesis):
    def __init__(self, vards, parole):
        super().__init__(vards,parole)

    def druka_vardu(self):
        print(f"Administrators {self.vards} ir izveidots")

vard1 = "Anna"
parole1 = "dators2"

vards2 = "Daina"
parole2 = "monitors2"

viesis1 = Viesis(vard1, parole1)
viesis1.druka_vardu()
viesis1.parbauda_paroli(parole1)

viesis2 = Darbinieks(vards2, parole2)
viesis2.druka_vardu()
viesis2.parbauda_paroli(parole2)