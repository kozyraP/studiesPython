dane_logowania = ('Admin', '1234')
lista_filmow = ['A', 'B', 'C']
lista_aktorow = ['X', 'Y', 'Z']
slownik_aktorow = {
    'X' : ['A'],
    'Y' : ['B', 'C'],
    'Z' : ['A', 'B', 'C']
    }
slownik_dostepnosci = {
    'A' : 5,
    'B' : 3,
    'C' : 0
    }
users = {
    'test' : 'password'
    }
uprawnienia = "user"

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
    if login == dane_logowania[0] and haslo == dane_logowania[1]:
        print('Logowanie powiodlo sie')
        uprawnienia = "admin"
    elif login in users:
        if users[login] != haslo:
            print('Logowanie nie powiodlo sie')
            continue
        else:
            uprawnienia = "user"
    else:
        print('Logowanie nie powiodlo sie')
        continue
 
    while True:
        print(10 * '*')
        print('MENU')
        print(10 * '*')
     
        print('1. Wyswietl wszystkie filmy')
        print('2. Wyswietl wszystkich aktorow')
        print('3. Wyswietl powiazania aktorow z filmami')
        print('4. Dodaj film lub aktora')
        print('5. Modyfikuj dane')
        print('6. Usun dane')
        print('7. Wypozycz film')
        if uprawnienia == "admin":
            print('8. Dodaj uzytkownika')
        print('0. Wyloguj')
     
        wybor = input('Prosze podac swoj wybor: ')
        if wybor == '1':
            for film in lista_filmow:
                print(film)
            wybor = input('Czy chcesz wrocic do menu? T/N: ')
            if wybor.upper() == 'T':
                continue
            else:
                break
        elif wybor == '2':
            for aktor in lista_aktorow:
                print(aktor)
            wybor = input('Czy chcesz wrocic do menu? T/N: ')
            if wybor.upper() == 'T':
                continue
            else:
                break
        elif wybor == '3':
            for aktor, film in slownik_aktorow.items():
                print(f"Aktor {aktor} wystepuje w filmach {film}")
            wybor = input('Czy chcesz wrocic do menu? T/N: ')
            if wybor.upper() == 'T':
                continue
            else:
                break
        elif wybor == '4':
            wybor = input('Czy chcesz dodac aktora czy film? A/F: ')
            if wybor == 'A':
                nowy_aktor = input('Prosze podac imie aktora: ')
                lista_aktorow.append(nowy_aktor)
                nowe_powiazania = input("Podaj gdzie gra ten aktor i odziel filmy przecinkiem i spacja -> ', '")
                slownik_aktorow[nowy_aktor] = nowe_powiazania.split(", ")
            elif wybor == 'F':
                nowy_film = input('Prosze podac nazwe filmu: ')
                lista_filmow.append(nowy_film)
                slownik_dostepnosci[nowy_film] = 1
        elif wybor == '5':
            print('1. Lista filmow')
            print('2. Lista aktorow')
            print('3. Powiazania aktorow z filmami')
     
            wybor = input('Ktore dane chcesz zmodyfikowac?: ')
            if wybor == '1':
                film = input('Prosze podac nazwe filmu: ')
                if film in lista_filmow:
                    nowa_nazwa = input('Prosze podac nowa nazwe filmu: ')
                    index_filmu = lista_filmow.index(film)
                    lista_filmow[index_filmu] = nowa_nazwa
            elif wybor == '2':
                aktor = input('Podaj aktora: ')
                if aktor in lista_aktorow:
                    nowa_nazwa = input('Prosze podac nowe imie aktora: ')
                    lista_aktorow[lista_aktorow.index(aktor)] = nowa_nazwa
            elif wybor == '3':
                aktor = input('Powiazania ktorego aktora chcesz zmodyfikowac? ') 
                if aktor in slownik_aktorow.keys():
                    nowe_powiazanie = input('Prosze podac nowe powiazanie aktora: ')
                    slownik_aktorow[aktor].append(nowe_powiazanie)
        elif wybor == '6':
            print('1. Lista filmow')
            print('2. Lista aktorow')
            print('3. Powiazania aktorow z filmami')
     
            wybor = input('Ktore dane chcialbys usunac? ')
            if wybor == '1':
                film = input('Ktory film chcesz usunac? ')
                if film in lista_filmow:
                    index_filmu = lista_filmow.index(film)
                    del lista_filmow[index_filmu]
                else:
                    print('Nie ma takiego elementu')
            elif wybor == '2':
                aktor = input('Którego aktora chcesz usunac? ')
                if aktor in lista_aktorow:
                    del lista_aktorow[lista_aktorow.index(aktor)]
                else:
                    print('Nie ma takiego elementu')
                    
            elif wybor == '3':
                aktor = input('Powiazania ktorego aktora chcesz usunac? ')
                if aktor in slownik_aktorow.keys():
                    slownik_aktorow[aktor] = []
                    
        elif wybor == '7':
            for film, dostepnosc in slownik_dostepnosci.items():
                print(f"Filmu {film} dostepne jest {dostepnosc} sztuk")
            film = input('Prosze podac nazwe filmu: ')
            if film in slownik_dostepnosci.keys():
                if slownik_dostepnosci[film] != 0:
                    print('Film wypozyczony pomyslnie')
                    slownik_dostepnosci[film] -= 1
                else:
                    print('Film aktualnie niedostepny')
            else:
                print('Film nie znajduje sie w wypozyczalni')
        elif wybor == '8' and uprawnienia == "admin":
            print(10 * '*')
            print('MENU')
            print(10 * '*')
            login = input("Podaj login nowego uzytkownika: ")
            haslo = input("Podaj haslo nowego uzytkownika: ")
            if login in users:
                print("Taki uzytkownik juz istnieje! ")
                cond = input(f"Czy chcesz nadac uzytkownikowi '{login}' nowe haslo? (y/n)")
                if cond == "y":
                    users[login] = haslo
            else:
                users[login] = haslo
            
        elif wybor == '0':
            break
