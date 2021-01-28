#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    c = n
    for i in range(n): 
        xx = i
        while xx < n - 1:
            xx+= 1
            if s[i] == s[xx]:
                c += 1
            else:
                if s[i:xx] == s[xx+1:2*xx-i+1]:
                    c += 1
                break

    return c
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
