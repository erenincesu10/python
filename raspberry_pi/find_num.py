# -*- coding: utf-8 -*-
# sayi_bul.py

from random import randint

sayi = randint(0,100)
tekrar = 0

while True:
  tekrar += 1
  tahmin = int(input("0-100 arasındaki tahmin ettiginiz sayiyi girin : ")
  if tahmin > sayi:
               print("Daha buyuk bir sayi girin!")
  elif tahmin < sayi:
               print("Daha kucuk bir sayi girin!")
  else:
               print("Tebrikler! Dogru sayiyi {} tahminde bildiniz.".format(tekrar))
               
               devam = input("Devam mi ? Tamam mi ? "D/T" :  ")
               devam = devam.upper()
               
               if devam == "D":
                      tekrar = 0
                      sayi = randint(0,100)
               else:
                      break
               
 print("Game Over")
       
