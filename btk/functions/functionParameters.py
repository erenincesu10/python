

"""
def changeName(n):
    n = "ada"

name = "yigit"

changeName(name)
print(name)
"""
"""
def change(n):
    n[0] = "istanbul"

sehirler = ["ankara","izmir"]

change(sehirler[:])

print(sehirler)
"""
"""
def add(*params):# tuple listesi göndermek için tek yıldız
    sum = 0
    for n in params:
        sum += n
    return sum

print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,50,60,10,20))
"""
"""
def displayUser(**args): #dict göndermek için
    for key,value in args.items():
        print("{} is {} ".format(key,value))


displayUser(name = "Çınar", age = 2, city = "istanbul")
displayUser(name = "Ada", age = 12, city = "kocaeli", phone = "123456")
displayUser(name = "Yiğit", age = 14, city = "ankara", phone = "123457")
"""

def myfunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myfunc(10,20,30,40,50,key1 = "value1",key2 = "value2")

