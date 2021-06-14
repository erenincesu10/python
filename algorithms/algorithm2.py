
n = int(input("0-100 arasında N sayısını giriniz : "))

if n > 80 and n <= 100:
    print("A")

else:
    if n > 60 and n <= 80:
        print("B")
    else:
        if n > 40 and n <= 60:
            print("C")
        else:
            if n > 20 and n <= 40:
                print("D")
            elif n <= 20 and n > 0:
                print("E")
            else:
                print("Hatalı girdi yaptınız!")

