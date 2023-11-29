
def fact(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return(f)

def coeff(n,r):
    y=fact(n)/fact(r)/fact(n-r)
    return(int(y))

print('Enter the no# of rows of pascals Trainagle: ',end='')
num=int(input())
print("The Pascal's Triangle with",num,"rows is shown below: ")
print("*******************************************")
for row in range(num):
    for space in range(row+1,num):
        print(' ',end='')
    for col in range(row+1):
        print(coeff(row,col),end=' ')
    print()
print("*******************************************")
