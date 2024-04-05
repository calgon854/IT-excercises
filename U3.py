import math

##-----------------------
##------------  Base
##-----------------------

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Strecke(Punkt):
    def __init__(self, p1, p2):
        super().__init__("Strecke")
        self.A = p1
        self.B = p2
    
    def distance(p1, p2):
        len = math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
        return len
        
##-----------------------
##------------  Main
##-----------------------
    
class Figur:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name    

    def Umfang(self):
        return 0

    def __str__(self):
        return self.name    

class Dreieck(Figur):
    def __init__(self, A, B, C):
        super().__init__("Dreieck")

        self.Ak = A  # Versuche Koordinaten weitergeben an str für Ausgabe
        self.Bk = B
        self.Ck = C

        self.AB = Strecke.distance(A,B)
        self.BC = Strecke.distance(B,C)
        self.CA = Strecke.distance(C,A)

        self.U = self.AB + self.BC + self.CA

    def Umfang(self):
        return self.U
        
    def __str__(self):
        return f"Umfang von {self.name} = {self.U}\nKoordinaten verwendet: {self.Ak},{self.Bk},{self.Ck}"       # weil oben variablen nicht ankommen, scheiterts hier

class Rechteck(Figur):
    def __init__(self, A, B, C, D):
        super().__init__("Rechteck")

        self.Ak = A  # Versuche Koordinaten weitergeben an str für Ausgabe
        self.Bk = B
        self.Ck = C
        self.Dk = D

        self.AB = Strecke.distance(A,B)
        self.BC = Strecke.distance(B,C)
        self.CD = Strecke.distance(C,D)
        self.DA = Strecke.distance(D,A)

        self.U = self.AB + self.BC + self.CD +self.DA 

    def Umfang(self):
        return self.U
        
    def __str__(self):
        return f"Umfang von {self.name} = {self.U}\nKoordinaten verwendet: {self.Ak},{self.Bk},{self.Ck},{self.Dk}"   # weil oben variablen nicht ankommen, scheiterts hier

class Kreis(Figur):
    def __init__(self, other, r):               # scheitert an zuviel / zuwenig variablen, gleiches problem wie oben - probleme mit other
        super().__init__(self, "Kreis")
        self.mittelpunkt = other
        self.radius = r

    def umfang(self):
        len = math.pi * self.radius*2
        return len
    
    def __str__(self):
        return f"Umfang von {self.name} = {self.U}\nKoordinaten verwendet: {self.Ak},{self.Bk},{self.Ck},{self.Dk}"  # ""

class Polygon(Figur):
    def __init__(self, other):              # gleiches problem wie bei kreis - schwierigkeiten mit other, weil potenziell unendlich seiten
        super().__init__("Polygon")

        self.Ak = A  # Versuche Koordinaten weitergeben an str für Ausgabe
        self.Bk = B
        self.Ck = C
        self.Dk = D

        self.AB = Strecke.distance(A,B)
        self.BC = Strecke.distance(B,C)
        self.CD = Strecke.distance(C,D)
        self.DA = Strecke.distance(D,A)

        self.U = self.AB + self.BC + self.CD +self.DA 

    def Umfang(self):
        return self.U
        
    def __str__(self):
        return f"Umfang von {self.name} = {self.U}\nKoordinaten verwendet: {self.Ak},{self.Bk},{self.Ck},{self.Dk}"   # weil oben variablen nicht ankommen, scheiterts hier


##-----------------------
##------------  Input
##-----------------------        

A = Punkt(1,4)
B = Punkt(2,2)
C = Punkt(3,6)
D = Punkt(5,8)
##------------
d = Dreieck(A,B,C)
r = Rechteck(A,B,C,D)
#k = Kreis(B,2)  
#p = Polygon(A,B,C,D)
  
print(r)


########################### Übung 4 verlief viel besser! Wirklich! 