#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoArrays function below.
def twoArrays(k, A, B):
    a=sorted(A)
    b=sorted(B, reverse=True)
    x=1
    i=0
    while i<len(a) and x>0:
        if a[i]+b[i]<k:
            x=0
        else:
            i+=1
    if x==1:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
