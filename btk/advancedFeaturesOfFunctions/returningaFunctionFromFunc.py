

"""
def usAlma(number):


    def inner(power):
        return number ** power

    return inner

two = usAlma(2)
print(two(3))
    #three = usAlma(3)
"""
"""
def yetki_sorgula(page):

    def inner(role):
        if role == "admin":
            return "{0} rolünün {1} sayfasına ulaşabilir".format(role,page)
        else:
            return "{0} rolünün {1} sayfasına ulaşamaz".format(role,page)

    return inner

user1 = yetki_sorgula("Product Edit")
print(user1("admin"))
print(user1("guest"))
"""

def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam

    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim

    if islem_adi == "toplama":
        return toplam
    else:
        return carpma

toplama = islem("toplama")
print(toplama(1,3,5,7,9))
