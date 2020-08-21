#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    s=0
    p=0
    ls=[]
    for i in range(len(contests)):
        s=s+contests[i][0]
        if contests[i][1]==1:
            p+=1
            ls.append(contests[i][0])
    x=p-k
    ls=sorted(ls)
    if x>0:
        for i in range(x):
            s=s-(2*ls[i])
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
