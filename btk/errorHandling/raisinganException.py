

"""
x = 10

if x > 5:
    raise Exception("x 5ten büyük değer alamaz!")
"""
"""
def check_password(parola):
    import re
    if len(parola) < 8:
        raise Exception("parola en az 7 karakter olmalıdır.")
    elif not re.search("[a-z]",parola):
        raise Exception("parola küçük harf içermelidir!")
    elif not re.search("[A-Z]",parola):
        raise Exception("parola büyük harf içermelidir!")
    elif not re.search("[0-9]",parola):
        raise Exception("parola rakam harf içermelidir!")
    elif not re.search("[_@$]",parola):
        raise Exception("parola alpha numeric karakter içermelidir!")
    elif not re.search("\s",parola):
        raise Exception("parola boşluk içermemelidir!")

password = "1234567aA_ "

try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("Geçerli parola : else")
finally:
    print("validation tanımlandı")
"""

class Person:
    def __init__(self,name,year):
        if len(name) > 10:
            raise Exception("name alanı fazla karakter içeriyor")
        else:
            self.name = name

p = Person("Fatiiiiiiiiiiiihhhhhhhhh",1985)
