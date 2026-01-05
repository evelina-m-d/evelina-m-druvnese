
from abc import ABC, abstractmethod  #importē palīgus abstraktajai klasei
import random #importē spēju vieglāk ģenerēt nejaušus skaitļus

class Robot(ABC):                     #vecākklase - abstrakta klase, vispārīga datu struktūra, kas nepieciešama visiem robotiem
    def __init__(self, name):
        self.name = name
        self.battery_level = random.randrange(1, 100) #ģenerē nejaušus skaitļus robotu baterijas līmeņiem

    @abstractmethod  #abstraktā metode - perform_task(), katra apakšklase to īsteno atšķirīgi
    def perform_task(self): 
        pass 

    def battery_status(self):            #kopīgā, nemainīgā metode visām apakšklasēm
        print(f"{self.name} baterijas līmenis: {self.battery_level}%")


class CleaningRobot(Robot):             #3 apakšklases, kur katra metodi(perform_task) realizē citādāk, nemantojot neko
    def perform_task(self):
        print(f"{self.name} sāk tīrīt!")

class SecurityRobot(Robot):
    def perform_task(self):
        print(f"{self.name} patrulē apkārtni!")

class CookingRobot(Robot):
    def perform_task(self):
        print(f"{self.name} gatavo ēst!")

roboti = [CleaningRobot("IRobot"), SecurityRobot("Roboguard"), CookingRobot("ChefBot")]    #saraksts ar visiem nepieciešamajiem objektiem, izmantojot visas pieejamās klases

for robots in roboti:
    robots.perform_task()       #iet cauri visiem robotiem sarakstā un izsauc tiem abas pieejamās metodes
    robots.battery_status()
    print("-" * 30)