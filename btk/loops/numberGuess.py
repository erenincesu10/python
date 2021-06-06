
import random

sayi = 0
trueNum = random.randint(1,100)
hak = int(input("Kaç hakkınız olsun : "))

while sayi != trueNum or hak != 0:

    sayi = int(input("Bir sayi giriniz : "))

    if sayi < trueNum:
        print("Daha yüksek bir sayı girişi yapınız")
        hak -= 1
        print(f"{hak} Hakkınız kaldı!")

    elif sayi > trueNum:
        print("Daha küçük bir sayı girişi yapınız")
        hak -= 1
        print(f"{hak} Hakkınız kaldı!")

    elif hak == 0:
        print("Haklarınız bitti maalasef bilemediniz!")
        print(f"Sayı : {trueNum}")
        break

    else:
        print("Tebrikler doğru bildiniz!")
        break
