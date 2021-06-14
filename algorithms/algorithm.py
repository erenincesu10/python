
a = []

i = 1

while i < 15:
    if i % 2 == 0:
        a.append(i)

    if len(a) > 5:
        print("Daha fazla ekleme yapılamaz!")
        a.remove(i)

    i += 1


print(a)
