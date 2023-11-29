#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'calc' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER c as parameter.
#

def calc(c):
    # Write your code here
    r=(c/(2*(math.pi)))
    a=((math.pi)*(r**2))
    #print(round(r,2),round(a,2))
    print("("+str(round(r,2))+", "+str(round(a,2))+")")

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    c = int(input().strip())

    #result = calc(c)

    #fptr.write(str(result) + '\n')

    #fptr.close()
    calc(c)
