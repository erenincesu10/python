# BANKAMATİK UYGULAMASI

ErenHesap = {
    'ad':'Eren Yılmaz',
    'hesapNo':'13245678',
    'bakiye': 3000,
    'ekHesap': 2000
}

AliHesap = {
    'ad' : 'Ali Turan',
    'hesapNo' : '12345678',
    'bakiye' : 2000,
    'ekHesap' : 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= miktar
        print("Paranızı alabilirsiniz!")
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if toplam >= miktar:
            ekHesapKullanimi = input("Ek hesap kullanılsın mı ? (E/H) : ")
            ekHesapKullanimi.upper()

            if ekHesapKullanimi == "E":
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print("Paranızı alabilirsiniz!")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bakiye bulunmaktadır!")
        else:
            print("Yetersiz Bakiye!")
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")

paraCek(ErenHesap, 3000)
print("*" * 50)
paraCek(ErenHesap, 2000)
