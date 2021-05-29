
sayilar = [1,3,5,7,9,12,19,21]

"""
1- sayilar listesindeki hangi sayilar 3'ün katıdır ?
for i in sayilar:
    if (i%3 == 0):
        print(i)
"""

"""
2- sayilar listesinde sayıların toplamı kaçtır ?
toplam = 0
for i in sayilar:
    toplam += i

print(toplam)
"""

"""
3- sayilar listesindeki tek sayıların karesini alıp toplamı yazdırınız.
toplam = 0
for i in sayilar:
    if i%2 == 1:
        toplam += i**2
print(f" Toplam = {toplam}")
"""
"""
sehirler = ["kocaeli","istanbul","ankara","izmir","rize"]

for sehir in sehirler:
    if (len(sehir) <= 5):
        print(sehir)
"""

"""
urunler = [
    {"name":"samsung s6",'price':'3000'},
    {"name": "samsung s7", 'price': '4000'},
    {"name": "samsung s8", 'price': '5000'},
    {"name": "samsung s9", 'price': '6000'},
    {"name": "samsung s10", 'price': '7000'}
]

5- Ürünlerin fiyatları toplamı nedir ?
toplam = 0
for urun in urunler:
    fiyat = int(urun['price'])
    toplam += fiyat

print(toplam)

# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz.
for urun in urunler:
    if (int(urun['price']) <= 5000):
        print(urun['name'])
"""
