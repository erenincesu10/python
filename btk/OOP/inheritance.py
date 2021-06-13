

# Inheritance (Kalıtım) : miras alma

class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("Person created")

    def who_am_i(self):
        print("I am a person")

    def eat(self):
        print("I am eating!")

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname) #run the Person init method
        self.studentNumber = number
        print("Student created")

    #override
    def who_am_i(self):
        print("I am a student!")

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname) #Person.init alternative
        self.branch = branch

    def who_am_i(self):
        print(f"I am a {self.branch} teacher")

p1 = Person("Ali","Yılmaz")
s1 = Student("Eren","Aslan",number= 1254)
t1 = Teacher("Serkan","Koc","Math")

print(p1.firstName + " " + p1.lastName)
print(s1.firstName + " " + s1.lastName + " " +  str(s1.studentNumber))

s1.who_am_i()
p1.who_am_i()
t1.who_am_i()
