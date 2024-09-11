
start = int(input('Ievadiet sākuma skaitli: '))
end = int(input('Ievadiet beigu skaitli: '))

for i in range(start, end+1):
    if i % 2 != 0:
        print(i, end=', ')



