

fruits = {"orange","apple","banana"}

#print(fruits[0]) indekslenemez

for i in fruits:
    print(i)


fruits.add("cherry")
print(fruits)

fruits.update(["mango","grape"])
print(fruits)
#tekrarlı elemanlar yazılmaz.

fruits.remove("mango")
fruits.discard("apple")
fruits.pop()#herhangi bir eleman silinir.
print(fruits)

fruits.clear()#bütün elemanlar silinir.
