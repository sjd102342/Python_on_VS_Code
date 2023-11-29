#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'func' function below.
#
# The function is expected to print an INTEGER.
# The function accepts following parameters:
#  1. INTEGER startvalue
#  2. INTEGER endvalue
#  3. INTEGER stepvalue
#

def rangefunction(startvalue, endvalue, stepvalue):
    # Write your code here
    startvalue=x
    endvalue=y
    stepvalue=z
    
    if startvalue >= 1:
        #for i in range(startvalue,(endvalue+1)):
        while startvalue <= endvalue :
            print(str(startvalue),end=' ')
            print(str(startvalue**2),end=' ')
            startvalue = startvalue + stepvalue
            
if __name__ == '__main__':

    x = int(input().strip())

    y = int(input().strip())

    z = int(input().strip())

    rangefunction(x, y, z)
