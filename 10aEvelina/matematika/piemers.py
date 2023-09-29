import math 
import random
skaitlis = 43.7
print('Noapaļots uz leju:',math.floor(skaitlis))
print('Noapaļots uz augšu:',math.ceil(skaitlis))

print('Mainīgā pakāpe:',math.pow(skaitlis,2))
print(math.pow(4,6)) #pirmais sk ir tas, ko kāpina bet otrais pakāpe
pakape = 3
print(math.pow(skaitlis, pakape))

print('Kvadrātsakne:',math.sqrt(skaitlis))

x = 256971/2641
print('x:', x)

print('Formatēts x: ' "%.3f"%x) #noapaļošana aiz komata


cipars = random.random() #0.1 - 1.0
print(cipars)

cipars2 = random.randint(1,50)
print(cipars2)