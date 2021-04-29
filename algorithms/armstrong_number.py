def armstrong(sayi):

    toplam = 0

    for rakam in str(sayi):
        toplam += int(rakam)**4

    if toplam == sayi:
        return True
    else:
        return False

for n in range(1000,10000):
    if armstrong(n):
        print(n,end=' ')

