
car_list = []

def add(name,brand,year):
    car_list.append({ 
        'Nosaukums': name,
        'Marka': brand,
        'Gads': year,
        })

def show():
    if car_list:
        print("\nMašīnas sarakstā: ")
        for car in car_list:
            print(f"Nosaukums: {car['Nosaukums']}, Marka: {car['Marka']}, Gads: {car['Gads']}")
    else: 
        print("\nSaraksts ir tukšs.")


def atjaunot(nosaukums,marka,gads):
    for masina in car_list:
        if masina["Nosaukums"] == nosaukums:
            masina["Marka"] == marka
            masina["Gads"] == gads

def dzest_masinu(nosaukums):
    for masina in car_list:
        if masina['nosaukums'] == nosaukums:
            car_list.remove(masina)
            print(f"Mašīna '{nosaukums}' dzēsta no saraksta.")
            return
        print(f"Mašīna '{nosaukums}' nav atrasta sarakstā.")

while True:
    print("\n izvēlēties darbību:")
    print("1. Pievienot mašīnu")
    print("2. Parādīt visas mašīnas")
    print("3. Atjaunināt mašīnu")
    print("4. Dzēst mašīnu")
    print("5. Iziet")

    izvele = input("izvēlies darbību (1-5):")
    if izvele == '1':
        nosaukums = input("Ievadiet mašīnas nosaukumu:")
        marka = input("Ievadiet mašīnas marku:")
        gads = int(input("Ievadiet mašīnas gadu:"))
        add(nosaukums,marka,gads)
    
    elif izvele == '2':
        show()

    elif izvele == '3':
        nosaukums = input("Ievadiet nosaukumu, kuru vēlaties atjaunināt:")
        jauna_marka = input("Ievadiet jauno marku:")
        jauns_gads = int(input("Ievadiet jauno gadu:"))
        '''Bus jaizsauc funkcija'''
    
    elif izvele == '4':
        nosaukums = input("Ievadiet mašīnas nosaukumu:")
        dzest_masinu(nosaukums)

    elif izvele == '5':
        print("Programma izbeigta.")
        break

    else:
        print("Nepareiza ievade. Mēģiniet vēlreiz!")
       