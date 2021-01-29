#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
from collections import Counter
def countTriplets(arr, r):
    lc=Counter()
    rc=Counter(arr)
    c=0
    for i in arr:
        rc[i]-=1
        n=lc[i/r]
        m=rc[i*r]
        c+=n*m
        lc[i]+=1
    return c
        
            
    
    return z
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
