

a = [4,8,3,1,18,9,21,20,5,17]
n = 0
size = len(a)

for i in range(1,size):
    for j in range(i-1,i):
        n = a[j+1]
        a[j+1] = a[j]
        a[j] = n

print(a)
