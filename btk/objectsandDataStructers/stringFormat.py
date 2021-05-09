

name = "Eren"
surName = "Kral"

"""süslü parantezin yerine name verisini yollar.
print("My name is {}".format(name))
"""

"""ikili format örneği
print("My all name is {} {}".format(name,surName))
"""
"""
print("My all name is {1} {0}".format(name,surName))
çıktı = My all name is Kral Eren
"""

"""
print("My all name is {n} {s}".format(n = name,s = surName))
"""

"""
result = 200 / 800
print("Result is {}".format(result))
3 virgülden sonra kaç sayı geleceğini söyler,1 soldan kaç basamak boşluk bırakılacağını söyler
print("Result is {r:1.3}".format(r = result))
"""

"""
fstring
print(f"My all name is {name} {surName}")
"""
