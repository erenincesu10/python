


birPuanliklar = ["A","a","E","e","I","i","L","l","N","n","O","o","R","r","S","T","t","U","u"]
ikiPuanliklar = ["D","d","G","g"]
ucPuanliklar = ["B","b","C","c","M","m","P","p"]
dortPuanliklar = ["F","f","H","h","V","v","W","w","Y","y"]
besPuanliklar = ["K","k"]
sekizPuanliklar = ["J","j","X","x"]
onPuanliklar = ["Q","q","Z","z"]


puan = 0

while puan < 100:

    kelime = input("Kelimeyi giriniz : ")

    for harf in kelime:
        if harf in birPuanliklar:
            puan += 1

        elif harf in ikiPuanliklar:
            puan += 2

        elif harf in ucPuanliklar:
            puan += 3

        elif harf in dortPuanliklar:
            puan += 4

        elif harf in besPuanliklar:
            puan += 5

        elif harf in sekizPuanliklar:
            puan += 8

        elif harf in onPuanliklar:
            puan += 10

    print(puan)

    if puan >= 100 :
        print("Tebrikler oyunu kazandınız !")
        quit()
