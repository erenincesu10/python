
"""
# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.

tekrar = int(input("Kaç kez ekrana yazdırılacağını giriniz : "))
kelime = input("Kelimeyi giriniz : ")

def yazdir(word, again):
    for i in range(again):
        print(word)

yazdir(kelime,tekrar)
"""
"""
# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon yazın

def listeyeCevir(*params):
    a = []
    for i in params:
        a.append(i)

    print(a)

listeyeCevir(10,20,30,560,"Hello World")
"""
"""
# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun
def asalSayilariBul(ilk,son):
    for sayi in range(ilk,son+1):
        for j in range(2,sayi):
            if (sayi % j == 0):
                break
        else:
            print(sayi)


start = int(input("Başlangıç sayısını giriniz : "))
end = int(input("Bitiş sayısını giriniz : "))

asalSayilariBul(start,end)
"""
"""
# 4- Kendisini gönderilen bir sayının tam bölenlerini bir liste içerisinde saklayan bir fonksiyon yazın.

def bolenler(sayi):
    bolen = []

    for i in range(2,sayi):
        if sayi % i == 0:
            bolen.append(i)

    print(bolen)

num = int(input("Sayiyi giriniz : "))

bolenler(num)
"""
