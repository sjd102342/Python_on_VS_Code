#!/bin/python3

import math
import os
import random
import re
import sys


def resume(first, second, parent, city, phone, start, strfind, string1):
    # Write your code here
    first1=first.strip().capitalize()
    second1=second.strip().capitalize()
    parent1=parent.strip().capitalize()
    city1=city.strip()
    print(first1,second1,parent1,city1)
    print(phone.isnumeric())
    if phone[0]==start:
        print(True)
    else:
        print(False)
    print(first.count(strfind)+second.count(strfind)+parent.count(strfind)+city.count(strfind))
    print(string1.split())
    print(city.find(strfind))


if __name__ == '__main__':

    a = input()

    b = input()

    c = input()

    d = input()

    ph = input()

    no = input()

    ch = input()

    str = input()

    resume(a, b, c, d, ph, no, ch, str)