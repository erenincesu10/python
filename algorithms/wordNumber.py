
cumle = input("Cümlenizi giriniz : ")
bosluk = 0

for karakter in cumle:
    if karakter == " ":
        bosluk=bosluk + 1

print("Kelime sayisi:{}".format(bosluk+1))
