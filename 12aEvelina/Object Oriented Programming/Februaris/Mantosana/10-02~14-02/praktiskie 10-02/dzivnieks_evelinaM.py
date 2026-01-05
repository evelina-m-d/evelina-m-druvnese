class Dzivnieks:
    def __init__(self, vards, vecums):
        self.vards = vards
        self.vecums = vecums

    def izdodSkanu(self):
        print("*insert animal sound here*")

class Kakis(Dzivnieks):
    def __init__(self, vards, vecums):
        super().__init__(vards,vecums)
    
    def izdodSkanu(self):
        print("Meow! /ᐠ-˕-マⳊ")

class Suns(Dzivnieks):
    def __init__(self, vards, vecums):
        super().__init__(vards,vecums)

    def izdodSkanu(self):
        print("Woof! ૮ >ﻌ< ა")

class Putns(Dzivnieks):
    def __init__(self, vards, vecums):
        super().__init__(vards,vecums)

    def izdodSkanu(self):
        print("Chirp! ꒰ঌ( •ө• )໒꒱")

kakitis = Kakis("Pele", 10)
kakitis.izdodSkanu()

sunitis = Suns("Bella", 7)
sunitis.izdodSkanu()

putnins = Putns("Dollija", 3)
putnins.izdodSkanu()