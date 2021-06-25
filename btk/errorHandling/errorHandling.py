

"""
try:
    x = int(input("x : "))
    y = int(input("y : "))
    print(x/y)
except (ZeroDivisionError, ValueError) as e :
    print("yanlış girdi yaptınız!")
    print(e)
"""
while True:
    try:
        x = int(input("x : "))
        y = int(input("y : "))
        print(x/y)
    except Exception as ex:
        print("yanlış girdi yaptınız!")
        print(ex)
    else:
        break
    finally:
        print("try except sonlandı!")

