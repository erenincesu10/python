
def hacimHesapla(yaricap,yukseklik):

    hacim = (yariCap**2) * 3.14 * yukseklik
    return hacim

yariCap = float(input("Yaricap degerini giriniz :"))
yukseklik = float(input("Yukseklik degerini giriniz : "))
print("Silindirin hacmi : ",hacimHesapla(yariCap,yukseklik))
