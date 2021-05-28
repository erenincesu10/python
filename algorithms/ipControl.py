

def IpKontrol(adres):
    try:
        bolumler = adres.split('.') #her bir liste elemanını kaydeder
        gecerli = 0

        for i in bolumler:
            if int(i)>= 0 and int(i)<=255:
                gecerli += 1
        if gecerli==4:
            return True
        else:
            return False
        #eğer try bloğunda bir hata olursa except bloğuna atlar ve except bloğundaki kodlar çalışır
    except:
        return False
    #print(bolumler)
for n in range(4):
    a = input("IP adresini giriniz: ")

    if IpKontrol(a):
        print(a,"Gecerli bir IP adresidir")
    else:
        print(a,"Geçersiz bir IP adresidir")
