row=int(input("Enter the no.# of rows: "))
num=0
for i in range(1,row+1):
    for k in range(i,row):
        print('*',end='')
    for j in range(1,i+1):
        num+=1
        print(num,end=' ')
        
    print()

print(num)
