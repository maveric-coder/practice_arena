#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.

def sherlockAndAnagrams(s):
    c=0
    ls={}
    for i in range(1,len(s)):
        for j in range(len(s)-i+1):
            z=str(sorted(s[j:j+i]))
            if z in ls:
                c+=ls[z]
                ls[z]+=1
            else:
                ls[z]=1
    return c
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
