
# key - value sistemiyle çalışır.


"""
sözlük tanımlama
plakalar = {"Kocaeli" : 41, "İstanbul" : 34}
print(plakalar["İstanbul"])

plakalar["Ankara"] = 6
print(plakalar)
"""

users = {
    "erenincesu" : {
        "age" : 20,
        "roles" : ["user"],
        "email" : "eren@gmail.com",
        "address" : "istanbul",
        "phone" : 111111
    },
    "emreincesu" : {
        "age" : 20,
        "roles" : ["admin","user"],
        "email" : "emre@gmail.com",
        "address" : "kars",
        "phone" : 222222
    }
}

print(users["erenincesu"])
