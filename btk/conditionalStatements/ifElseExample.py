
import datetime

"""
1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.

name = input("İsminizi giriniz : ")
age = int(input("Yasinizi giriniz : "))
edu = input("Okul bilginizi giriniz : ")

if age >= 18 and (edu == "Üniversite" or edu == "Lise"):
    print(f"Sayın {name} Ehliyet alma hakkına sahipsiniz!")
else:
    print("Ehliyet almak için yeterli özelliklere sahip değilsiniz!")
"""

"""
2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırınız.

exam1 = float(input("1.yazılı notunuzu giriniz : "))
exam2 = float(input("2.yazılı notunuzu giriniz : "))
sozlu = float(input("Sozlu notunuzu giriniz : "))

ortalama = (exam1 + exam2 + sozlu)/3

if (ortalama >= 0) and (ortalama <= 24):
    print(f"Ortalamanız : {ortalama} Notunuz : 0")
elif (ortalama > 24) and (ortalama <= 44):
    print(f"Ortalamanız : {ortalama} Notunuz : 1")
elif (ortalama > 44) and (ortalama <= 54):
    print(f"Ortalamanız : {ortalama} Notunuz : 2")
elif (ortalama > 54) and (ortalama <= 69):
    print(f"Ortalamanız : {ortalama} Notunuz : 3")
elif (ortalama > 69) and (ortalama <= 84):
    print(f"Ortalamanız : {ortalama} Notunuz : 4")
elif (ortalama > 84) and (ortalama <= 100):
    print(f"Ortalamanız : {ortalama} Notunuz : 5")
"""

"""
3- Trafiğe çıkış tarihi alınan bir aracın servis zamanı aşağıdaki bilgilere göre hesaplayınızç
    #1. Bakım => 1.Yıl
    #2. Bakım => 2.Yıl
    #3. Bakım => 3.yıl
    #** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
    #*** datetime modulünü kullanmanız gerekiyor.

tarih = input("Aracınız hangi tarihte trafiğe çıktı (2019/8/9) :")
tarih = tarih.split("/")

trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days

if days <= 365:
    print("1.servis aralığı")
elif days >365 and days <= 365*2:
    print("2.servis aralığı")
elif days > 365*2 and days <= 365*3:
    print("3.servis aralığı")
"""
