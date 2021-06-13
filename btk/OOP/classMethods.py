
"""
class Person:
    #class attributes
    address = 'no info'
    #constructor (yapıcı metod)
    def __init__(self, name, year): #self represents the obj
        # object attributes
        self.name = name
        self.year = year


    #instance methods
    def intro(self):
        print("Hello there. I am " + self.name)

    def calculateAge(self):
        return 2021 - self.year



# object (instance)
p1 = Person(name = "Eren",year = 2001) #define a object
p2 = Person(name = "Veli",year = 1999)

p1.intro()
p2.intro()

print(f"Adım : {p1.name} Yaşım : {p1.calculateAge()}")
print(f"Adım : {p2.name} Yaşım : {p2.calculateAge()}")
"""

class Circle:
    pi = 3.14

    def __init__(self, yaricap = 1):
        self.yaricap = yaricap

    #Methods

    def cevreHesapla(self):
        return 2*self.pi*self.yaricap

    def alanHesapla(self):
        return self.pi*(self.yaricap**2)


c1 = Circle(15)

print(f"alan : {c1.alanHesapla()} cevre : {c1.cevreHesapla()}")
