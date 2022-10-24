def is_leap(year):
    leap = False
    if(year <= 100000 and year >= 1900):
        if(year%4 == 0 and year%100 != 0):
            leap = True
        elif(year%400 == 0):
            leap = True 
        else:
            leap = False
    else:
        print("Wrong number")   
    
    return leap

year = int(input())
print(is_leap(year))
