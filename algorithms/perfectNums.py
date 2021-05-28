

def mukemmelSayi(sayi):
    toplam = 1

    for bolen in range(2,(sayi//2)+1):
        if sayi%bolen == 0:
            toplam += bolen

    if toplam == sayi:
        return True
    else:
        return False


for n in range(2,1000):
    if mukemmelSayi(n):
        print(n,end='-')

