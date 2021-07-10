

#The generator generates an iterator that does not occupy memory.
"""
def cube():


    for i in range(5):
       yield i**3 # we can access the data just 1 time.

for i in cube():
    print(i)
"""

generator = (i**3 for i in range(5)) #if we use () instead of [], we create a generator.

print(generator)

print(next(generator))
print(next(generator))
print(next(generator))
