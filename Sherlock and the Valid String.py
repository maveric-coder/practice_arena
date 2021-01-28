#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
from collections import Counter

def isValid(c):
    zz=Counter(c)
    #print(zz)
    d = Counter(Counter(c).values())
    #print(d.values())
    #print(d)
    if len(d)==1:
        return "YES"
    if len(d)>2:
        return "NO"
    if 1 in d.values() and (d[min(d.keys())]==1 or (max(d.keys()) - min(d.keys())==1)):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
