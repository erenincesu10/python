
"""

name = "Eren İncesu"

for letter in name:
    if letter == "e":
        continue
    print(letter)
#break döngüden çıkış yapar. continue ise o andaki kısmı boş geçip devam eder.
"""

"""
x = 0

while x < 5:
    x += 1
    if x == 2:
        continue
    print(x)
"""


"""
1-100 ' e kadar tek sayıların toplamı

i = 0
result = 0
while i < 100:
    i += 1
    if i%2 == 0:
        continue
    result += i
    print(i)
    
print(f"toplam : {result}")
"""
