
a = int(input("a sayisini giriniz : "))
b = int(input("b sayisini giriniz : "))
c = int(input("c sayisini giriniz : "))

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)
