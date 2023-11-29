
L=int(input("Enter the Limit : "))
print("And the Prime No.s within the limit are : ",end='')
for i in range(1,L):
    if i>1:
        for a in range(2,i):
            if i%a == 0:
                #print(i," : is not a prime No.")
                break
        else:
                print(i,' ',end='')
            
###    else:
###        print(i," : is not in range")      