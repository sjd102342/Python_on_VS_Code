
def fact(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return(f)

def coeff(n,r):
    y=fact(n)/fact(r)/fact(n-r)
    return(int(y))

#print(1)

for row in range(4):
    for col in range(row+1):
        print(coeff(row,col),end=' ')
    print()
