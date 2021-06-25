import random

#result = dir(random)
#result = help(random)

result = random.random() #0.0 - 1.0 arası sayı üretir
result = random.uniform(1,10) # 1.0 - 10.0 sayı üretir
result = random.randint(1,5) # 1 - 5 arası int üretir

names = ["eren","ahmet","mehmet","james"]
#result = names[random.randint(0,len(names)-1)]
result = random.choice(names)

liste = list(range(0,10))
random.shuffle(liste)

liste = range(100)
result = random.sample(liste,3)

print(result)
