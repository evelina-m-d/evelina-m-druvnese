
class Laiks:
    def __init__ (self, stundas=0, minutes=0, sekundes=0):
        self.stundas = stundas
        self.minutes = minutes
        self.sekundes = sekundes

    def uzstadit_laiku(self, stundas, minutes, sekundes):
        self.stundas = stundas
        self.minutes = minutes
        self.sekundes = sekundes

        #pieliek nulles cipara priekšā
        #ja laiks ir rakstīts tikai ar vienu ciparu

        if(stundas>=0 and stundas <=9):
            self.stundas = str(stundas).zfill(2)
        if(minutes>=0 and minutes <=9):
            self.minutes = str(minutes).zfill(2)
        if(sekundes>=0 and sekundes <=9):
            self.sekundes = str(sekundes).zfill(2)

    def izvadit_laiku(self):
        print("Laiks ir ", self.stundas,":", self.minutes, ":", self.sekundes)

    def nakama_stunda(self):
        if (self.stundas == 23):
            self.stundas = 0
            self.stundas = str(self.stundas).zfill(2)
        else:
            self.stundas = self.stundas + 1
        

laiks1 = Laiks(23, 30, 49)
laiks1.izvadit_laiku()

laiks1.nakama_stunda()
laiks1.izvadit_laiku()

laiks1.uzstadit_laiku(3,3,3)
laiks1.izvadit_laiku()
