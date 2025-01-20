
class Students:
    def __init__ (self, vards, uzvards, vecums, kursa_numurs):
        self.vards = vards
        self.uzvards = uzvards
        self.vecums = vecums
        self.kursa_numurs = kursa_numurs

    def parbaudit(self):
        if self.vecums < 18 or self.kursa_numurs < 1 or self.kursa_numurs > 4:
            print("Ievadiet pareizus datus!")
            return True
        else:
            return False
    
    def izvadit(self):
        print(f"********************************\nStudenta dati: \nStudents: {self.vards} {self.uzvards} \nVecums: {self.vecums} \nKurss: {self.kursa_numurs}. kurss \n********************************")
        
vards = input("Ievadiet studenta vārdu:")
uzvards = input("Ievadiet studenta uzvārdu:")

while True:
    try:
        vecums = int(input("Ievadiet studenta vecumu:"))
        kursa_numurs = int(input("Ievadiet kursa numuru:"))

        students1 = Students(vards, uzvards, vecums, kursa_numurs)
        if students1.parbaudit() == False:
            students1.izvadit()
            break
   
    except ValueError:
        print("Ievadiet piemērotu skaitli!")    

        

