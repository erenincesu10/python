def basamakToplam(x , y):
    sayi = x**y
    print(sayi)
    toplam = 0

    for rakam in str(sayi):
        toplam += int(rakam)

    return toplam

taban = int(input("Taban degerini giriniz : "))
us = int(input("Us degerini giriniz :"))

print(basamakToplam(taban , us))
