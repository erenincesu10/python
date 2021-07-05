


"""
with open("newfile.txt","r+",encoding='utf-8') as file:
    print(file.read())

with open("newfile.txt","r+",encoding='utf-8') as file:
    file.seek()
    file.write("deneme")

with open("newfile.txt","r+",encoding='utf-8') as file:
    print(file.read())
"""
# update at the end of the page.
"""
with open("newfile.txt","a",encoding='utf-8') as file:
    file.write("\nAslan incesu")

with open("newfile.txt","r",encoding='utf-8') as file:
    print(file.read())
"""

# update at the top of the page
"""
with open("newfile.txt","r+",encoding='utf-8') as file:
    content = file.read()
    content = "Emre incesu\n" + content
    file.seek(0)
    file.write(content)

with open("newfile.txt","r",encoding='utf-8') as file:
    print(file.read())
"""

# update at the middle of the page
with open("newfile.txt","r+",encoding='utf-8') as file:
    list = file.readlines()
    list.insert(1,"Yılmaz incesu\n")
    file.seek(0)
    file.writelines(list)

with open("newfile.txt","r",encoding='utf-8') as file:
    print(file.read())
