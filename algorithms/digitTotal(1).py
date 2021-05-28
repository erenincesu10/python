
def basamakToplam(sayi):
    toplam = 0
    for i in sayi:
        toplam += int(i)**2

    print(toplam)


number = input("Iki basamakli bir sayi giriniz : ")
basamakToplam(number)
