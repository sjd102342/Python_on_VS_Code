#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'calculateGrade' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts 2D_INTEGER_ARRAY students_marks as parameter.
#

def calculateGrade(students_marks):
    s=[]
    for i in students_marks:
        avg = int(sum(i)/len(i))
        if avg >= 90:
            s.append("A+")
            #return s
        elif avg in range(80, 90):
            s.append("A")
            #return s
        elif avg in range(70, 80):
            s.append("B")
            #return s
        elif avg in range(60, 70):
            s.append("C")
            #return s
        elif avg in range(50, 60):
            s.append("D")
            #return s
        elif avg in range(0, 50):
            s.append("F")
            #return s
    return s

if __name__ == '__main__':


    students_marks_rows = int(input("How many Students: ").strip())
    students_marks_columns = int(input("How many Subjects: ").strip())

    students_marks = []

    for _ in range(students_marks_rows):
        students_marks.append(list(map(int, input("Enter Marks: ").rstrip().split())))

    result = calculateGrade(students_marks)

    print(result)
