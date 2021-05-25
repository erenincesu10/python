

#x = 5
#y = 10
#z = 20

x, y, z = 5 ,10 ,20

#x ,y = y , x

"""
x += 5  # ile aynı x = x + 5
x *= 5  # ile aynı x = x*5
x /= 5  # ile aynı x = x/5
x %= 5  # ile aynı x = x % 5
x //= 5 # ile aynı x = x // 5 
x **= 5 # ile aynı x = x ** 5 
"""
#print(x,y,z)

values = 1,2,3
print(values)
print(type(values))

x ,y , z = values #3ten az eleman olursa yeterli olmaz,3ten fazla olursa da fazla olduğu için yeterli olmaz fakat fazlalık durumuda *z yaparsak kalan elemanları z'ye liste olarak atar.

print(x,y,z)

