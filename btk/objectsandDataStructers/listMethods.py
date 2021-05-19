

numbers = [1,10,5,16,4,9,10]
letters = ["a","g","s","b","y","a","s"]

#listedeki min elemanı alma
val = min(numbers)

#listedeki max elemanı alma
val = max(numbers)

#listede bir elemandan diğerine kadar alma
val = numbers[3:6]

#listedeki bir elemanın değerini değiştirme
numbers[4] = 40

#istediğimiz yere bir eleman ekleme
numbers.insert(3,78)

#listeye eleman ekleme
numbers.append(49)

#listeden eleman silme(index numarasıyla)
numbers.pop(0)

#listeden eleman silme(elemanın değeriyle)
numbers.remove(10)

#listeyi sıralama
numbers.sort()

#listeyi tam tersine çevirme
numbers.reverse()

#listedeki elemanı saydırma
print(numbers.count(10))

#listedeki tüm elemanları silme
numbers.clear()

print(val)
print(numbers)
