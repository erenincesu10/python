
def asalMi(sayi):
    for i in range(2,sayi):
        if sayi%i == 0:
            return False
        else:
            return True

num = int(input("Bir sayi giriniz : "))

print(asalMi(num))
