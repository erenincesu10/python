

kareToplamı= 0
toplamKare = 0
fark = 0
kare = 0
toplam = 0
for i in range(0,101):
    kare = i**2
    kareToplamı = kareToplamı + kare


for i in range(0,101):
    toplam = toplam + i
    toplamKare = toplam**2


fark = toplamKare - kareToplamı
print(toplamKare,kareToplamı,fark)
