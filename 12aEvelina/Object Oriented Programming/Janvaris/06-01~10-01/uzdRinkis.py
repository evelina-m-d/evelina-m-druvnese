
class Rinkis:
    def __init__ (self, radiuss):
        self.radiuss = radiuss
        if self.radiuss <= 0:
            self.radiuss = 1
        else:
            self.radiuss = radiuss
    def izvadit_radiusu(self):
        return f"Rādiuss ir {self.radiuss}."
    def diametrs(self):
        return f"Diametrs ir {self.radiuss * 2}."

rinkis1 = Rinkis(0)
rinkis2 = Rinkis(3)

print(rinkis1.diametrs())
#print(rinkis2.diametrs())