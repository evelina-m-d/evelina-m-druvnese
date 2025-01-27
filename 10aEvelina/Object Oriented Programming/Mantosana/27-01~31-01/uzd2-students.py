
class Persona:
    def __init__(self,vards,vecums):
        self.vards = vards
        self.vecums = vecums
    def dati(self):
        print(f"{self.vards}, {self.vecums} gadi")


class Students(Persona):
    def __init__(self,vards,vecums,kurss):
        super().__init__(vards,vecums)
        self.kurss = kurss
    def dati(self):
        print(f"{self.vards}, {self.vecums} gadi, {self.kurss}. kurss")

cilveks1 = Persona("Eva", 19)
cilveks1.dati()

students1 = Students("Līva", 20, 3)
students1.dati()

super(Students, students1).dati() #parāda studentu tikai ar Persona filtru (no vārda, vecuma, kursa parāda tikai vārdu un vecumu)
    