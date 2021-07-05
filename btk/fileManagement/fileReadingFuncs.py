

with open("newfile.txt","r",encoding='utf-8') as file: #with ile komutlar bittikten sonra dosya kapanıcak
    content = file.read(10)
    print(content)
    file.seek(0)# sends the cursor to the entered value
    print(file.tell())#gives a cursors loc
    content2 = file.read()
    print(content2)
