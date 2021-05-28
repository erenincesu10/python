

def yerDegistir(a,b):
    print("ilk degerler : ",a,b)
    gecici = a
    a = b
    b = gecici
    print("A = {} , B = {}".format(a,b))

A = input("A degerini girin : ")
B = input("B degerini girin : ")

yerDegistir(A,B)
