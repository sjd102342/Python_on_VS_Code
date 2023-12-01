#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'sumOfNFibonacciNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def sumOfNFibonacciNumbers(n):
    # Write your code here
    if n>=1 and n<=100:
        f0=0
        f1=1
        a=[]
        count=0
        while count < n :
           a.append(f0)
           fn=f0+f1
           f0=f1
           f1=fn
           #a.append(fn)
           count += 1
        sum=0
        for i in a:
            sum=sum+i
    return(sum)
n=int(input("Enter the no.# of fibonacci Elements:"))
result = sumOfNFibonacciNumbers(n)
print("Sum of",n,"Fibocacci Elements is:",result)