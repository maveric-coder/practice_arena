#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
from collections import Counter
def makeAnagram(a, b):
    za = Counter(a)
    zb = Counter(b)
    print(za,zb)
    za.subtract(zb)

    return sum(abs(i) for i in za.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
