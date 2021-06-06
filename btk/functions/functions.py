

def sayHello(name = "user"): #parametre gönderilmezse "user" otomatik döndürür
    return  "Hello " + name


msg = sayHello("Eren")
print(msg)

def total(num1,num2):
    return num1 + num2

result = total(10,20)

print(result)

def yasHesapla(dogumYili):
    return 2021 - dogumYili

ageEren = yasHesapla(1957)
ageEmre = yasHesapla(2006)

def EmekliligeKacYilKaldi(dogumYili, isim):
    '''
    DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldi
    INPUT:  Dogum yili
    OUTPUT: Hesaplanan yil bilgisi
    '''

    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f"emekliliginize {emeklilik} yıl kaldı")
    else:
        print("Zaten emekli oldunuz!")

EmekliligeKacYilKaldi(1950,"Eren")
