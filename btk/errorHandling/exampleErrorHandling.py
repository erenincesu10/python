

"""
liste = ["1","2","5a","10b","abc"]

# 1- Find the numeric values in list elements.

for i in liste:
    try:
        result = int(i)
        print(result)
    except ValueError:
        continue
"""
"""
while True:
    sayi = input("sayı : ")
    if sayi == "q":
        break

    try:
        result = float(sayi)
        print("girdiğiniz sayı: ",result)
        break
    except:
        print("geçersiz sayı")
        continue
"""
"""
# 3- give a Turkish char error in the entered password.
def check_password(psw):
    turkce_karakterler = "şçğüöıİ"



    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Parola türkçe karakter içeremez")
        else:
            pass
    print("geçerli parola")

parola = input("Parola : ")

try:
    check_password(parola)
except TypeError as err:
    print(err)
"""
"""
# 4- create the factorial func and give error messages for the value that comes the function.

def factorial(x):
    x = int(x)

    if x < 0:
        raise ValueError("Negatif değer")

    result = 1

    for i in range(1,x+1):
        result *= i

    return result

for x in [5,10,20,-4,"10b"]:
    try:
        y = factorial(x)
    except ValueError as err:
        print(err)
        continue
    print(y)
"""
