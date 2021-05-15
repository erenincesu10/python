

message = 'Hello there. My name is Eren Incesu'

"""string harflerini büyük harfe çevirir
message = message.upper()
print(message)
"""

"""string harflerini küçük harfe çevirir
message = message.lower()
print(message)
"""

"""string kelimelerinin baş harflerini büyük karaktere çevirir
message = message.title()
print(message)
"""

"""string ifadenin sadece ilk karakterini büyük yapar
message = message.capitalize()
print(message)
"""

"""string ifadenin başındaki boşluk karakterini siler.
message = ' Hello there. My name is Eren Incesu'
message = message.strip()
print(message)
"""

"""string ifadeyi boşluklarından ayırıp bir diziye dönüştürür.
message = message.split()#split içerisine bir parametre gönderirsek o parametreden sonra ayırır.
print(message)
"""

"""ayrılmış string ifadeyi tekrardan birleştirir
message = ' '.join(message)#' ' yerine '*' deseydik aralara boşluk yerine yıldız koyacaktır.
print(message)
"""

"""string ifade içerisinden istediğimiz ifadeyi bulma
index = message.find('Eren')
print(index)#ifadenin ilk harfinin kaçıncı indexte olduğu bilgisini verir.Eğer "-1" değerini döndürürse kelime yoktur.
"""

"""başlangıç harfini bulma
isFound = message.startswith("H")
print(isFound)
"""

"""son harfini bulma
isFound = message.endswith("u")
print(isFound)
"""

"""string ifadeleri değiştirme
message = message.replace("Eren","Kral")
print(message)
"""

"""string bilgisini parametre kadarlık bir string içerisinin ortasına alır.
message = message.center(100)
print(message)
"""

"""string bilgisinin sağına ve soluna farklı ifade koyma
message = message.center(50,"*")
print(message)
"""
