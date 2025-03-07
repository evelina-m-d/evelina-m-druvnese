
class Varonis:
    def __init__(self, vards, dzivibas):
        self. vards = vards
        self.dzivibas = dzivibas

    def uzbrukt(self):
        print("*ieroča skaņa*")

class Karotajs(Varonis):
    def __init__(self, vards, dzivibas):
        super().__init__(vards, dzivibas)

    def uzbrukt(self):
        print("Karotājs uzbrūk ar zobenu!! ⚔")

    def aizstaveties(self):
        print("Karotājs atkal uzbrūk ar zobenu jo viņš māk tikai to! ⚔ ⚔ ⚔")

class Burvis(Varonis):
    def __init__(self, vards, dzivibas):
        super().__init__(vards, dzivibas)

    def uzbrukt(self):
        print("Burvis šauj uguns bumbu!! 🔥")

    def aizstaveties(self):
        print("Burvis uztaisa uguns vairogu! 🔥🔥🔥")

class Savejs(Varonis):
    def __init__(self, vards, dzivibas):
        super().__init__(vards, dzivibas)

    def uzbrukt(self):
        print("Šāvējs šauj bultu!! 🏹")

    def aizstaveties(self):
        print("Šāvējs mūk krūmos! 🍃")     


fiziskaisKarotajs = Karotajs("Eula", "7/10")
fiziskaisKarotajs.uzbrukt()
fiziskaisKarotajs.aizstaveties()

ugunsBurvis = Burvis("Yanfei", "9/10")
ugunsBurvis.uzbrukt()
ugunsBurvis.aizstaveties()

vejaSavejs = Savejs("Venti", "5/10")
vejaSavejs.uzbrukt()
vejaSavejs.aizstaveties()