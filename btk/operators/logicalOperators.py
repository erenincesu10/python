

x = 6
hak = 5
devam = "e"
result = 5 < x < 10

#and Birisi yanlış olursa False döndürür.İkisi de True olursa sonuç True olur.
result = (x > 5) and (x < 10)
result = (hak > 0) and (devam == "e")

#or Biris doğru olursa True döndürür.İkisi de False olursa sonuç False olur.
result = (x > 5) or (x%2 == 0)

#not Tam tersi
result = not (x > 0)

print(result)
