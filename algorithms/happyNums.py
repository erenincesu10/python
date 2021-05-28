

def mutluSayi(sayi):
    toplam = 0
    sayilar = []

    while True:
        for b in str(sayi):
            toplam += int(b)**2

        sayi = toplam

        if sayi in sayilar:
            break
        else:
            sayilar.append(sayi)
        toplam = 0

    if sayi == 1:
        return True
    else:
        return False

for n in range(2,21):
    if mutluSayi(n):
        print(n)
