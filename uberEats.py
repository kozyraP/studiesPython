restauracje = {
    'McDonald' : ['frytki', 'cola', 'burger'],
    'KFC' : ['frytki', 'cola', 'wings'],
    'Kebab' : ['cienki', 'cola', 'gruby'],
    'PizzaHut' : ['pizza', 'pepsi']
    }
listaZamowien = {}

clients = {
    'user1' : '1234',
    'user2' : '1234'
    }
delivers = {
    'deliver' : '1234',
    'deliver2' : '1234',
    'deliver3' : '1234',
    'deliver4' : '1234'
    }
restaurants = {
    'McDonald' : '1234',
    'KFC' : '1234',
    'Kebab' : '1234',
    'PizzaHut' : '1234'
    }
orders = {
    'order' : '1234',
    'order2' : '1234',
    'order3' : '1234'
    }

while True:
    print(10 * '*')
    print('1. Zaloguj')
    print('0. Zakoncz')
    print(10 * '*')
    wybor = input('Prosze podac swoj wybor: ')
    if wybor == "1":
        pass
    elif wybor == "0":
        print('Do zobaczenia :)')
        break
    else:
        print("ERROR")
        break
    
    login = input('Prosze podac login: ')
    haslo = input('Prosze podac haslo: ')
#client *******************************************
    if login in clients:
        if clients[login] != haslo:
            print('Logowanie nie powiodlo sie')
            continue
        else:
            print("Zalogowano jako klient")
            
            while True:
                print(10 * '*')
                print('MENU')
                print(10 * '*')
             
                print('1. Nowe zamowienie')
                print('2. Wyswietl restauracje')
                print('3. Wyswietl menu restauracji')
                print('0. Zakoncz')
                
                wybor = input('Prosze podac swoj wybor: ')
                print(wybor)

                if wybor == '1':
                    print(10 * '*')
                    print('Dostepne restauracje: ')
                    for nazwa in restauracje.keys():
                        print(nazwa)
                    wybor = input('Prosze podac swoj wybor: ')
                    if wybor in restauracje.keys():
                        print(10 * '*')
                        print('Dostepne dania:')
                        for danie in restauracje[wybor]:
                            print(danie)
                        order = input('Prosze podac swoj wybor: ')
                        if order in restauracje[wybor]:
                            listaZamowien[login] = order + ' z ' + wybor
                            print(10 * '*')
                            print(f"Uzytkownik {login} zamowil: {listaZamowien[login]}")
                        else:
                            print('Nieprawidlowa pozycja')
                    else:
                        print('Nieprawidlowa pozycja')
                    
                elif wybor == '2':
                    print(10 * '*')
                    print('Dostepne restauracje: ')
                    for nazwa in restauracje.keys():
                        print(nazwa)
                        
                elif wybor == '3':
                    print(10 * '*')
                    print('Dostepne restauracje: ')
                    for nazwa in restauracje.keys():
                        print(nazwa)
                    wybor = input('Prosze podac swoj wybor: ')
                    if wybor in restauracje.keys():
                        print(10 * '*')
                        print('Dostepne dania:')
                        for danie in restauracje[wybor]:
                            print(danie)
                    else:
                        print('Nieprawidlowa pozycja')
                else:
                    break
                
#restaurant ******************************************* 
    elif login in restaurants:
        if restaurants[login] != haslo:
            print('Logowanie nie powiodlo sie')
            continue
        else:
            print("Zalogowano jako restauracja")

            while True:
                print(10 * '*')
                print('MENU')
                print(10 * '*')
             
                print('1. Dodanie nowego dania')
                print('2. Usunięcie dania')
                print('3. Odczytanie listy dań')
                print('4. Modyfikacja nazwy któregoś z obecnych dań')
                print('0. Zakoncz')
                
                wybor = input('Prosze podac swoj wybor: ')
                print(wybor)

                if wybor == '1':
                    restauracje[login].append(input('Podaj nazwe nowego dania '))
                    print("Dodano nowe danie. ")
                    
                elif wybor == '2':
                    print(10 * '*')
                    print('Dostepne dania: ')
                    for nazwa in restauracje[login]:
                        print(nazwa)
                    wybor = input('Prosze podac swoj wybor: ')
                    if wybor in restauracje[login]:
                        indexDania = restauracje[login].index(wybor)
                        del restauracje[login][indexDania]
                        print("Usunieto " + wybor)
                    else:
                        print("Nie znaleziono dania: " + wybor)
                        
                elif wybor == '3':
                    print(10 * '*')
                    print('Dostepne dania: ')
                    for nazwa in restauracje[login]:
                        print(nazwa)

                elif wybor == '4':
                    print(10 * '*')
                    print('Dostepne dania: ')
                    for nazwa in restauracje[login]:
                        print(nazwa)
                    wybor = input('Prosze podac nazwe dania do modyfikacji: ')
                    if wybor in restauracje[login]:
                        indexDania = restauracje[login].index(wybor)
                        restauracje[login][indexDania] = input('Podaj nowa nazwe dania: ')
                    else:
                        print("Nie znaleziono dania: " + wybor)
                    
                else:
                    break
#dostawca *******************************************          
    elif login in delivers:
        if delivers[login] != haslo:
            print('Logowanie nie powiodlo sie')
            continue
        else:
            print("Zalogowano jako dostawca")

            while True:
                print(10 * '*')
                print('MENU')
                print(10 * '*')
             
                print('1. Wyswietl liste zamowien')
                print('0. Zakoncz')
                
                wybor = input('Prosze podac swoj wybor: ')
                if wybor == '1':
                    print(listaZamowien)
                else:
                    break
           

#zamowienia *******************************************          
    elif login in orders:
        if orders[login] != haslo:
            print('Logowanie nie powiodlo sie')
            continue
        else:
            print("Zalogowano jako obsluga zamowien")

            while True:
                print(10 * '*')
                print('MENU')
                print(10 * '*')
                print('1. Wyswietl informacje na temat klientow, dostawcow i restauracji')
                print('2. Wyswietl liste zamowien')
                print('0. Zakoncz')
                
                wybor = input('Prosze podac swoj wybor: ')
                if wybor == '1':
                    print(10 * '*')
                    print(" Klienci: ")
                    for cl in clients.keys():
                        print(cl)
                    print(" Dostawcy: ")
                    for cl in delivers.keys():
                        print(cl)
                    print(" Restauracje: ")
                    for cl in restaurants.keys():
                        print(cl)
                    print(10 * '*')
                elif wybor == '2':
                    print(listaZamowien)
                else:
                    break
            
    else:
        print('Logowanie nie powiodlo sie')
        continue
    
