
class Kaste:
    def __init__(self, malas_garums, krasa):
        #malas garums var but no 2-10, ja neatbilst, tad uzstādīt default 2
        if malas_garums>=2 and malas_garums<=10:
            self.malas_garums = malas_garums
        else:
            print("malas garums neatbilst!")
            self.malas_garums = 2
        self.krasa = krasa