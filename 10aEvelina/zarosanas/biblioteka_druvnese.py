print('Bibliotēkas sistēma.\n Ievadi vienā vai dažos vārdos, ar lielo burtu un garumzīmēm!\n') #paskaidrojums lietotājam

neNo = (input('Vai pie tevis atrodas laikā nenodots izdevums?\n')) #pirmais jautājums, no tā atkarīgs vai vispār var saņemt izdevumu
if neNo == 'Jā':
    print('Nevari saņemt izdevumu.')
elif neNo == 'Nē':
    piepIzd = (input('Vai izdevums ir pieprasīto izdevumu sarakstā, parasta grāmata vai žurnāls?\n')) #otrais jautājums, no tā atkarīgs dienu skaits
    if piepIzd == 'Žurnāls':
        print('Vari saņemt izdevumu uz 7 dienām.')
    if piepIzd == 'Pieprasīto izdevumu sarakstā':
        print('Vari saņemt izdevumu uz 2 dienām.')
    elif piepIzd == 'Parasta grāmata':
        perStu = (input('Esi personāls vai students?\n'))  #trešais jautājums, no tā atkarīgs parastas grāmatas izsniegšanas dienu skaits
        if perStu == 'Personāls':
            print('Vari saņemt izdevumu uz 28 dienām.')
        if perStu == 'Students':
            print('Vari saņemt izdevumu uz 14 dienām.')
else:
    print('Pārbaudi, vai ir ievadīts pareizi, ar garumzīmēm!') #pasaka, vai kaut kas ir nepareizi ievadīts

    
    



