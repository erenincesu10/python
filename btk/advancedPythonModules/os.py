

import os
import datetime

#result = dir(os)
#result = os.name #nt means windows os



#changes the directory
#os.chdir('C:\\Users\Casper\PycharmProjects\ALGORİTMALAR')
#os.chdir('C:\\')

#gives info about where are we
#result = os.getcwd()

#creates folder
#os.mkdir("newdirectory")

#creates a nested folder
#os.makedirs("newdirectory/eren")

#renaming a directory
#os.rename("newdirectory","yeniklasor")

#deleting a dir
#os.rmdir("new_dir")

#listing
#result = os.listdir()
#result = os.listdir("C:\\")
#for dosya in os.listdir():
#    if dosya.endswith(".py"):
#        print(dosya)

#result = os.stat("kod.py")
#result = datetime.datetime.fromtimestamp(result.st_ctime)#creating time
#result = datetime.datetime.fromtimestamp(result.st_atime)#last access time
#result = datetime.datetime.fromtimestamp(result.st_mtime)#modify time

#running a program
#os.system("notepad.exe")

#path

result = os.path.abspath("kod.py")
result = os.path.dirname(os.path.abspath("kod.py"))
result = os.path.exists("kod.py")#checks the existence of the file
result = os.path.isdir("C:\\Users\Casper\PycharmProjects\ALGORİTMALAR")
#result = os.path.join("C:\\","deneme")
#result = os.path.split("C:\\deneme")
#result = os.path.splitext("kod.py")

print(result)
