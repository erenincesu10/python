
"""
sayilar = [1,3,5,7,9,12,19,21]
# 1- sayilar listesini while ile ekrana yazdırın.
i = 0
while i < len(sayilar):
    print(sayilar[i])
    i += 1
"""

"""
2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.
start = int(input("Başlangıç değerini girin : "))
stop = int(input("Bitiş değerini girini : "))

sayi = start 

while (sayi < stop):
    if sayi%2 == 1:
        print(sayi)

    sayi += 1
"""
"""
3- 1-100 arasındaki sayıları azalan şekilde yazdırın.

i = 100
while i>0:
    print(i)
    i -= 1
"""

"""
i = 0
sayilar = []
while i<5:
    sayi = int(input(f"{i+1}. sayiyi giriniz : "))
    sayilar.append(sayi)
    i += 1

sayilar.sort()
j = 0
while j < len(sayilar):
    print(sayilar[j])
    j += 1
"""
"""
# 5- Kullanıcıdan alacağınınz sınırsız ürün bilgisini urunler listesinde saklayınız
#    Ürün sayısını kullanıcıya sorun.
#    dictionary listesi yapısı (name,price) şeklinde olsun.
#    Ürün ekleme işlemi bittiğinde ürünleri ekranda while ile yazdırın.

elemanSayi = int(input("Girmek istediğiniz eleman sayısını veriniz : "))
urunler = []
i = 0

while i < elemanSayi:
    name = input(f"{i+1} Ürün ismi : ")
    price = input(f"{i+1} Ürün fiyatı : ")
    urunler.append({
        'name':name,
        'price':price
    })
    i += 1

for urun in urunler:
    print(f'ürün adı : {urun["name"]} ürün fiyatı : {urun["price"]}')
"""
