

#1. uzdevums

def ierakstit():
    with open('file.txt', 'a', encoding='utf-8', newline='') as fails:
        fails.write(input('Ievadiet savu tekstu:') + '\n')

#ierakstit()


#2. uzdevums

def nolasit():
    try:
        with open('file.txt', 'r', encoding='utf-8', newline='') as fails:
            dati = fails.readlines()
            print("Teksts failā:")
            for ieraksts in dati:
                    print(ieraksts.strip())
    except FileNotFoundError:
        print("Fails nepastāv!")

nolasit()


#3. uzdevums
