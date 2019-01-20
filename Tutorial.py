names=["kasia","aleksandra","kalina","patrycja"]
def say_hello(imie):
    if len(imie)==4:
        print("Hej",imie)
    else:
        print("Czesc",imie)
def nazwa_funkcji():
    print("Hej")
say_hello(names)
for name in names:
    say_hello(name)
class Vehicle:
    def __init__(self,kolor_karoserii,liczba_kol):
        self.kolor_karoserii=kolor_karoserii
        self.liczba_kol=liczba_kol
class Car(Vehicle):
    def __init__(self,kolor_karoserii):
        super().__init__(kolor_karoserii,4)

mycar=Car("red")
print(mycar.liczba_kol)
