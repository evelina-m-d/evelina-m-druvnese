
import time

def atzimes():
    while True:    
        try:
            rezultats = float(input("Ievadiet testa rezultātu (0-100): ")) #lietotāja ievade
            if rezultats > 100 or rezultats < 0:
                raise InterruptedError #ja ievade nav atbilstošajā diapazonā, neļauj turpināt un liek ievadīt vēlreiz
            elif rezultats >= 0 and rezultats <= 10:
                print(f"{rezultats}% : 1 (ļoti, ļoti vāji 😢)")  #pārbauda vērtējuma kvalitāti
            elif rezultats > 10 and rezultats <= 20:
                print(f"{rezultats}% : 2 (ļoti vāji 😪)")
            elif rezultats > 20 and rezultats <= 30:
                print(f"{rezultats}% : 3 (vāji 😐)")
            elif rezultats > 30 and rezultats <= 40:
                print(f"{rezultats}% : 4 (gandrīz viduvēji 🙄)")
            elif rezultats > 40 and rezultats <= 53:
                print(f"{rezultats}% : 5 (viduvēji 😦)")
            elif rezultats > 53 and rezultats <= 66:
                print(f"{rezultats}% : 6 (gandrīz labi 😮)")
            elif rezultats > 66 and rezultats <= 76:
                print(f"{rezultats}% : 7 (labi 😊)")
            elif rezultats > 76 and rezultats <= 86:
                print(f"{rezultats}% : 8 (ļoti labi 😜)")
            elif rezultats > 86 and rezultats <= 94:
                print(f"{rezultats}% : 9 (teicami 😇)")
            elif rezultats > 94 and rezultats <= 100:
                print(f"{rezultats}% : 10 (izcili 🤩)")
            nobeigums()
        except ValueError:
            print("Lūdzu ievadiet skaitli.") #nepareiza skaitļa gadījumā izprintē kļumi
        except InterruptedError:
            print("Lūdzu ievadiet skaitli diapazonā no 1-100.")
        
def nobeigums():
    while True:
            turpinat = input("Vai vēlaties ievadīt citu atzīmi? (j/n):")  #lietotājs ievada vai vēlas beigt
            if turpinat == 'n':
                print("Programma beidzas.")
                time.sleep(0.5)
                print("Programma beidzas..")
                time.sleep(0.5) 
                print("Programma beidzas...")
                time.sleep(0.8)
                print("Programma beigusies. Paldies! 👋")
                quit() 
            elif turpinat == 'j':
                break
            else:
                print("Ievadiet atbildi j/n formātā.")
    
    
atzimes()
    
    