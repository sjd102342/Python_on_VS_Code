def is_leap(year):
    leap = False
    if year in range(1900,100000):
        #if ((year%400 ==0) and (year%100!= 0)) or (year % 4 == 0):
        if ((year%4 ==0) and (year%100!= 0)) or (year % 400 == 0):  
            leap = True
    
    return leap

year = int(input())
print(is_leap(year))