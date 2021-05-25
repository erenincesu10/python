
"""
    ogrenciler = {
        "120" : {
            "ad" : "Ali",
            "soyad" : "Yılmaz",
            "telefon" : "532 000 00 01"
        },
        "125" : {
            "ad" : "Can",
            "soyad" : "Korkmaz",
            "telefon" : "532 000 00 02"
        },
        "128" : {
            "ad" : "Volkan",
            "soyad" : "Yükselen",
            "telefon" : "532 000 00 03"
        },
    }
"""

ogrenciler = {}


number = input("Öğrenci no : ")
name = input("Öğrenci adı : ")
surname = input("Öğrenci soyadı : ")
phone = input("Öğrenci telefon : ")

"""
ogrenciler[number] = {
    "ad" : name,
    "soyad" : surname,
    "telefon" : phone,
}"""

ogrenciler.update({
    number : {
        "ad" : name,
        "soyad" : surname,
        "telefon" : phone
    }
})

number = input("Öğrenci no : ")
name = input("Öğrenci adı : ")
surname = input("Öğrenci soyadı : ")
phone = input("Öğrenci telefon : ")

ogrenciler.update({
    number : {
        "ad" : name,
        "soyad" : surname,
        "telefon" : phone
    }
})

number = input("Öğrenci no : ")
name = input("Öğrenci adı : ")
surname = input("Öğrenci soyadı : ")
phone = input("Öğrenci telefon : ")

ogrenciler.update({
    number : {
        "ad" : name,
        "soyad" : surname,
        "telefon" : phone
    }
})
print("*"*50)

ogrenciNo = input("Öğrenci no giriniz : ")
print(ogrenciler[ogrenciNo])

print(f"Aradığınız {ogrenciNo} nolu öğrencinin adı : {ogrenciler['ad']} soyadı : {ogrenciler['soyad'] } telefonu ise : {ogrenciler['telefon']} ")
