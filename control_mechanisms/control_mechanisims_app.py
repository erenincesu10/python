print("""
[1] TOPLAMA İŞLEMİ
[2] ÇIKARMA İŞLEMİ
[3] ÇARPMA İŞLEMİ
[4] BÖLME İŞLEMİ
[5] ÜS ALMA İŞLEMİ
[Q] ÇIKIŞ



    """)



giris = input("Seçenek seçiniz :")

if giris == "1":
    x = input("İlk sayı    : ")
    x = float(x)
    y = input("İkinci sayi :")
    y = float(y)

    print("İşlem sonucu : ",x + y)
elif giris == "2":
    x = input("İlk sayi :")
    x = float(x)
    y = input("İkinci sayi :")
    y = float(y)

    print("İşlem sonucu :",x - y)

elif giris == "3":
    x = input("Birinci sayi : ")
    x = float(x)
    y = input("İkinci sayi :")
    y = float(y)

    print("İşlem sonucu :",x * y)

elif giris == "4":
    x = input("Birinci sayi :")
    x = float(x)
    y = input("İkinci sayi  :")
    y = float(y)

    print("İşleminizin sonucu :",x/y)

elif giris == "5":
    x = input("Taban  :")
    x = float(x)
    y = input("Kuvvet :")
    y = int(y)

    print("İşlem sonucu :",x**y)

elif giris == "q" or giris == "Q":
    print("Çıkılıyor...")
    quit()

else:
    print("Hatalı girdiniz!")
    quit()




