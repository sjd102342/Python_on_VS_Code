
a=int(input("Enter the Limit.# : "))
if a>1:
    for i in range(2,a):
        if a%i == 0:
            print(a," : is not a prime No.")
            break
    else:
            print("The no. ",a," is a prime No.")
        
else:
    print(a," : is not a prime No.")        