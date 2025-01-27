
import csv

class Doktorats:
    def __init__(self): #konstruktoram nav parametru jo sākotnējie dati nav zināmi 
        self.nosaukums = ""   #vērtības aizpildās vēlāk izmantojot ievadīšanas metodi
        self.pac_skaits = ""

    def ievadit_datus(self):
        self.nosaukums = input("Ievadiet doktorāta nosaukumu:")  #lietotājs pats ievada nepieciešamos datus

        while True: 
            try:
                self.pac_skaits = int(input("Ievadiet doktorāta pacientu skaitu: "))  
                if len(str(self.pac_skaits)) > 0:   #ja pacientu skaits ir tukša vieta, neļauj turpināt
                    saglabajamais = []
                    saglabajamais.append([self.nosaukums, self.pac_skaits])  #pievieno datus list, lai tos varētu saglabāt failā pēc tam

                    with open('Doktorati.csv', 'a', encoding='utf-8', newline='') as fails:  #atver failu un izmanto append lai to papildinātu, bet tikai tad, ja visi dati ievadīti līdz galam bez kļūmēm
                        writer = csv.writer(fails)
                        writer.writerows(saglabajamais) #pieraksta list failam
                    
                    break
                else:
                    print("Jāievada pareizs pacientu skaits!")
            except ValueError: #ja ievada kaut ko, kas nav skaitlis 
                print("Lūdzu ievadiet derīgu pacientu skaitu!") #liek atkārtot ievadi

        
    
    def izvadit_datus(self):  #glīti parāda lietotāja ievadītos datus uz ekrāna
        print("*****************************\nDOKTORĀTA DATI\n*****************************") 
        print(f'Doktorāts "{self.nosaukums}" apkalpo {self.pac_skaits} pacientus.')
 
Doktorats1 = Doktorats()  #tiek definēts objekts pēc klases
Doktorats1.ievadit_datus()  #tiek izsauktas abas objekta funkcijas atbilstošā secībā
Doktorats1.izvadit_datus()