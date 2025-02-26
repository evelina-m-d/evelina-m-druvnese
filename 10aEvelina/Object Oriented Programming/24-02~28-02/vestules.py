
from abc import ABC, abstractmethod #importē palīgus abstraktajai klasei

class Persona(ABC):
    def __init__(self, vards, epasts):
        self.vards = vards
        self.epasts = epasts

class Vestule:
    def __init__(self, sutitajs, sanemejs, saturs):
        self.sutitajs = sutitajs
        self.sanemejs = sanemejs
        self. saturs = saturs

class VestulesSuta(ABC):
    
    @abstractmethod
    def sutit_vestuli(self):
        pass

    @abstractmethod
    def sanemt_vestuli(self):
        pass


class Pastnieks(VestulesSuta):
    def sutit_vestuli(self, vestule):
        print("💌")
        print(f"Vēstule no: {sutijums.sutitajs.vards} <{sutijums.sanemejs.epasts}>")
        print(f"Vēstule uz: {sutijums.sanemejs.vards} <{sutijums.sanemejs.epasts}>")
        print(f'Ziņojums: "{sutijums.saturs}" \n')

    def sanemt_vestuli(self, vestule):
        print(f"Vēstule saņemta no: {sutijums.sutitajs.vards} <{sutijums.sanemejs.epasts}>")
        print(f"Vēstule adresēta uz: {sutijums.sanemejs.vards} <{sutijums.sanemejs.epasts}>")
        print(f'Ziņojums: "{sutijums.saturs}"')
        print("💌")

janisz = Persona("Jānis Zibens", "zibens.sper@svg.lv")
zanep = Persona("Zane Puķe", "pukes.zied@svg.lv")
vestule = "Sveiki, vai šodien esat darbā?"

sutijums = Vestule(janisz, zanep, vestule)

pastnieks1 = Pastnieks()
pastnieks1.sutit_vestuli(sutijums)
pastnieks1.sanemt_vestuli(sutijums)