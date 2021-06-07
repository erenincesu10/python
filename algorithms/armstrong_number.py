def armstrong(sayi):

    total = 0

    for rakam in str(sayi):
        total += int(rakam)**4

    if total == sayi:
        return True
    else:
        return False

for n in range(1000,10000):
    if armstrong(n):
        print(n,end=' ')

