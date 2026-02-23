
#divvirzienu rinda - autobuss, kur pasazieri var izkāpt pa abām pusēm
from collections import deque
autobuss = deque()

#pasazieri kapj
autobuss.append("Anna")
autobuss.append("Jānis")
autobuss.appendleft("Šoferis") #kāpj pa priekšējām durvīm
autobuss.append("Pēteris")

print("Autobusā:" , autobuss)

print("Izkāpj:", autobuss.popleft())
print("Izkāpj:", autobuss.pop())

#vienvirziena rinda - pusdienu rinda skolā
rinda=[]

rinda.append("Anna")
rinda.append("Jānis")
rinda.append("Pēteris")

print(rinda)
#apkalpos divus skolēnus
apkalpots1=rinda.pop(0)
apkalpots2=rinda.pop(0)

print("Palika rindā:", rinda)