

website = "www.erenincesu.com"
course = "Python Kursu : Bastan Sonra Python Programlama Rehberiniz (40 saat)"

"""
1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin
result = ' Hello World '
result = result.strip()
print(result)
#sağdan boşluk karakteri silme rstrip()
#soldan boşluk karakteri silme lstrip()
"""

"""
2- 'www.erenincesu.com' içindeki erenincesu bilgisi haricindeki her karakteri silin.
result = "www.erenincesu.com".strip("w.com")
print(result)
"""

"""
3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
course = course.lower()
print(course)
"""
"""
4- 'website' içinde kaç tane a karakteri vardır ? (count('a')
sum = course.count('e')
print(sum+1)
"""

"""
5- 'website' "www" ile baslayip "com" ile bitiyor mu ?
isStart = website.startswith("www")
isEnd = website.endswith("com")
if isStart == True and isEnd == True:
    print("Evet bitiyor")
else:
    print("Hayır bitmiyor")
"""

"""
6- 'website' içinde ".com" ifadesi var mı ?
isHave = website.find(".com")
isHave = website.rfind(".com") sağdan bulmaya çalışır
result = website.index("com")

if isHave > 0:
    print("Evet var")
else:
    print("Hayır yok")
"""

"""
7- 'course' içindeki karakterlerin hepsi alfabetik mi ? (isalpha, isdigit = rakam mı ?)
result = course.isalpha()
print(result)
"""

"""
8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna "*" ekleyiniz
yeni = "Contents"
yeni = yeni.center(50,"*")
yeni = "Contents".ljust(50,"*") sola yaslar rjust sağa yaslar
print(yeni)
"""

"""
9- 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin
course = course.replace(" ","-")
print(course)
"""

"""10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin.
result = "Hello World".replace("World","There")
print(result)
"""

"""
11- 'course' karakter dizisini boşluk karakterlerinden ayırın.
course = course.split(" ")
print(course)
"""
