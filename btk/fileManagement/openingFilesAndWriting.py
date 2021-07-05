
# open() function uses for opening file and creating a file
# Usage : open(file_name,file_access_mode)
# file_access_mode => it specifies for what purpose we opened the file

# "w" : Write mode. Creates the file at the location.
#   **Creates the file at the location.
#   **Deletes the file contents and re-adds
"""
file = open("newfile.txt","w") #we assign it to a variable because we will make an operation on it.
file.close()
file = open("D:/newfile.txt","w")
print(file)
"""
"""
file = open("newfile.txt","w",encoding='utf-8') #utf-8 allows the recognize Turkish char.
file.write("Eren incesu")
file.close()
"""

# "a" : Append. If the file doesnt exist in loc, creates a file.
#   ** The cursor always resumes from the end.
"""
file = open("newfile.txt","a",encoding='utf-8')
file.write("\nEren incesu")
file.close()
"""

# "x" : create mode. If the file already exist it gives an error.

file = open("newfile2.txt","x",encoding='utf-8')


# "r" : read mode. default. If the file doesnt exist at the location it gives an error.


