saraksts = [3,4,5,6,7,8,9,10]
saraksts.append('Cepums') #pievieno beigās
print(saraksts)

#izmet no beigām
saraksts.pop()
print(saraksts)

saraksts.insert(3, 'Hello') #ievieto pirms 3. no kreisas puses
print(saraksts)

saraksts.remove(6) #izdzēš norādīto vērtību
print(saraksts)


tests = [1,2,3,4,5,6,7,8]
del tests[2] #izdzes vienu elementu
print(tests)

del tests[3:6]
print(tests) #izdzes intervalu

cipari = [1,2,3,4,5,6,7,8]
del cipari[2:7:2] #no 2 lidz 7 dzes ara katru otro
print(cipari)