
enUzun = 0
aranan = 0

for sayi in range(999999, 300000, -1):
    zincir = 0
    n = sayi
    while n != 1:
        zincir += 1
        if n%2 == 0:
            n //=  2 
        else:
            n = 3*n + 1

    if zincir > enUzun:
        enUzun = zincir
        aranan = sayi

print("Zincir sayısı : ",enUzun,"Sayı : ",aranan)
