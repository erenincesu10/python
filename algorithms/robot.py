def basaDondur(hareket):
    X,Y = 0,0   #ilk 0 x'i temsil eder,diğer 0 y'yi temsil eder
    hareket = hareket.upper()

    for h in hareket:
        if h == "U":
            Y += 1
        elif h == "D":
            Y -= 1
        elif h == "L":
            X-= 1
        elif h == "R":
            X += 1
    if X == 0 and Y == 0:
        return True
    else:
        return False

def basadondurMine(hareket):

    hareket = hareket.upper()
    if hareket.count("L") == hareket.count("R") and hareket.count("D")==hareket.count("U"):
    #count() fonksiyonu string içindeki istediğimiz parametreyi sayar
        return True
    else:
        return False

for n in range(5):
    hareket = input("Robotun Hareketlerini Giriniz : ")
    if basadondurMine(hareket):
        print("Robot başlangıç noktasında")
    else:
        print("Robot başlangıç noktasında değil!")
