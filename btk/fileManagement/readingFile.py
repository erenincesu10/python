

"""
try:
    file = open("newfile.txt","r")
except FileNotFoundError:
        print("Dosya okuma hatası!")
finally:
    print("Dosya kapandı!")
    file.close()
"""

file = open("newfile.txt","r",encoding='utf-8')

# for döngüsü
"""
for i in file:
    print(i,end="")

file.close()
"""

#read() func
"""
content1 = file.read()

print("içerik 1")
print(content1)

content2 = file.read()
print("içerik 2")
print(content2)

file.close()
"""
"""
content = file.read(5) # first 5 char
content = file.read(3) # first 3 char after from 5 char
print(content)
"""

# readline()
"""
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline())
"""

# readlines() it makes a list with all lines

liste = file.readlines()
print(liste)
