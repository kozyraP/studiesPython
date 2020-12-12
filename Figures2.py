import math

class Figura:

    def __init__(self):
        self.nazwa = None
        self.pole = None
        self.obwod = None

    def wydrukuj_informacje(self):
        print(f'Nazwa: {self.nazwa}')
        print(f'Pole: {self.pole}')
        print(f'Obwod: {self.obwod}')

class Trojkat(Figura):

    def __init__(self, boki:list):
        try:
            if len(boki) != 3:
                raise TypeError
            
            if not self.czyTrojkatJestPrawidlowy(boki):
                raise ValueError
            
            self.init(boki)
            
        except TypeError:
            print(f'Trojkat musi miec 3 boki\nPodales {len(boki)}')
            
        except ValueError:
            print('Nieprawidlowa dlugosc bokow trojkata')

    def czyTrojkatJestPrawidlowy(self, boki:list):
        return boki[0] + boki[1] > boki[2] and boki[1] + boki[2] > boki[0] and boki[0] + boki[2] > boki[1]

    def init(self, boki:list):
        super().__init__()
        self.nazwa = 'Trojkat'
        self.boki = boki
        self.pole = self.oblicz_pole()
        self.obwod = self.oblicz_obwod()

    def oblicz_pole(self):
        p = self.oblicz_obwod() / 2
        return math.sqrt(p * (p - self.boki[0]) * (p - self.boki[1]) * (p - self.boki[2]))

    def oblicz_obwod(self): 
        return self.boki[0] + self.boki[1] + self.boki[2]


class Prostokat(Figura):

    def __init__(self, a, b):
        super().__init__()
        self.nazwa = 'Prostokat'
        self.a = a
        self.b = b
        self.pole = self.oblicz_pole()
        self.obwod = self.oblicz_obwod()
 

    def oblicz_pole(self):
        return self.a * self.b

    def oblicz_obwod(self): 
        return 2 * self.a + 2 * self.b
 
class Kwadrat(Prostokat):

    def __init__(self, a):
        super().__init__(a,a)
        self.nazwa = 'Kwadrat'

class Kolo(Figura):

    def __init__(self, promien):
        super().__init__()
        self.nazwa = 'Kolo'
        self.promien = promien
        self.pole = self.oblicz_pole()
        self.obwod = self.oblicz_obwod()

    def oblicz_pole(self):
        return self.promien ** 2 * 3.14 

    def oblicz_obwod(self):
        return self.promien * 2 * 3.14 

    def wydrukuj_informacje(self):
        super().wydrukuj_informacje()
        print(f'Promien: {self.promien}')
 
