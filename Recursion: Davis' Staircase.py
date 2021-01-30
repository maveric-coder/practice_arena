#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
ls={}
def stepPerms(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    if n not in ls:
        ls[n]=stepPerms(n-1)+stepPerms(n-2)+stepPerms(n-3)
    return ls[n]
    
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
