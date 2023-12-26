#To find largest odd no. in a String of numbers
s=input("Enter the no. String: ")
l=[]
if s.isnumeric()==True:
    for i in s:
        b=int(i)
        if b%2!=0:
            l.append(b)
    print("The largest odd no. in",s,"is:",max(l))
else:
    print("Entered String",s,"is not a number string")


