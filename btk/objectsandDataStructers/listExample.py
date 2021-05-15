
"""
1- "BMW, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
carBrand = ["BMW","Mercedes", "Opel", "Mazda"]
"""

"""
2- Liste kaç elemanlıdır ?
print(len(carBrand))
"""

"""
3- Listenin ilk ve son elemanı nedir ?
firstElement = carBrand[0]
lastElement = carBrand[-1]
print(firstElement,lastElement)
"""

"""
4- Mazda değerini Toyota ile değiştirin.
carBrand[-1] = "Toyota"
print(carBrand)
"""

"""
5- Mercedes listenin bir elemanı mıdır ?
isHave = "Mercedes" in carBrand
print(isHave)
"""

"""
6- Listenin -2 indeksindeki değer nedir ?
eksiIki = carBrand[-2]
"""

"""
7- Listenin ilk 3 elemanını alın.
result = carBrand[0:3]
print(result)
"""

"""
8- Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
carBrand[-2:] = ["Toyota", "Renault"]
"""

"""
9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
lastList = carBrand + ["Audi","Nissan"]
print(lastList)
"""

"""
10- Listenin son elemanını silin.
del carBrand[-1]
result = carBrand
print(result)
"""

"""
11- Liste elemanlarını tersten yazdırınız.
result = carBrand[::-1]
print(result)
"""

"""
12- Aşağıdaki verileri bir liste içerisinde saklayınız.
    #studentA : Yiğit Bilgi 2010, (70,60,70)
    #studentB : Sena Turan 1999, (80,80,70)
    #studentC : Ahmet Turan 1998, (80,70,90)

studentA = ["Yiğit","Bilgi",2010,[70,60,70]]
studentB = ["Sena","Turan",2010,[80,80,70]]
studentC = ["Ahmet","Turan",2010,[80,70,90]]
"""

"""
13- Liste elemanlarını ekrana yazdırınız.
print(studentA[0])
print(studentB[1])
print(studentC[3][1])

print(f"{studentA[0]} {studentA[1]} {2021-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])//3}")
"""
