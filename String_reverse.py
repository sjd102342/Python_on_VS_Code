
s=input('Enter String: ')
len=len(s)
s1=''
for i in range(1,len+1):
    s1=s1+s[-i]
print('Using for loop - reverse print of',s,'is:',s1)

print('Using Slicing - reverse print of',s,'is:',s[-1::-1])

rev=reversed(s)
#print('reverse print of:',rev)
print('Using Reversed function - reverse print of:',''.join(rev))