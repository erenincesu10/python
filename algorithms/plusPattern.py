sutun = int(input("Kac sutunlu arti olusturmak istediginizi belirtiniz(Tek sayi girmeye dikkat edin!) : "))

if sutun % 2 == 0 :
    print("Hatali girdi yaptiniz!")

else:
    for i in range(sutun):
        if i == (sutun//2):
            for j in range(sutun):
                print('X',end='')
            print(end="\n")

        else:
            for j in range(sutun):
                print(' ',end='')
                if j == (sutun//2)-1 :
                    print('X')
