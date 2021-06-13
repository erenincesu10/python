
#class

class Person:
    #class attributes
    address = 'no info'
    #constructor (yapıcı metod)
    def __init__(self, name, year): #self represents the obj
        # object attributes
        self.name = name
        self.year = year
        print("init metodu çalıştı")

    #methods


# object (instance)
p1 = Person(name = "Eren",year = 2001) #define a object
p2 = Person(name = "Veli",year = 1999)

#updating
p2.name = "ali"

#accessing obj attributes
print(f"name : {p1.name} year : {p1.year} address : {p1.address}")
print(f"name : {p2.name} year : {p2.year}")


