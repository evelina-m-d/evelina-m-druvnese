
import math

class Forma:
    def __init__(self):
        pass

    def aprekinatLaukumu(self):
        return 0

class Kvadrats(Forma):
    def __init__(self):
        pass

    def aprekinatLaukumu(self):
        mala = float(input("Ievadiet malas garumu:"))
        laukums = mala ** 2
        print(f"Kvadrāta (☐ ) laukums ir {laukums}!")

class Taisnsturis(Forma):
    def __init__(self):
        pass

    def aprekinatLaukumu(self):
        mala = float(input("Ievadiet 1. malas garumu:"))
        mala2 = float(input("Ievadiet 2. malas garumu:"))
        laukums = mala * mala2
        print(f"Taisnstūra (𓊌) laukums ir {laukums}!")

class Aplis(Forma):
    def __init__(self):
        pass

    def aprekinatLaukumu(self):
        radiuss = float(input("Ievadiet radiusu:"))
        laukums = round((radiuss * 2 * math.pi), 2)
        print(f"Apļa (⚪ ) laukums ir {laukums}!")

kvadratins = Kvadrats()
kvadratins.aprekinatLaukumu()

taisnsturitis = Taisnsturis()
taisnsturitis.aprekinatLaukumu()

aplitis = Aplis()
aplitis.aprekinatLaukumu()
 