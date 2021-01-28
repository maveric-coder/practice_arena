#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
from collections import Counter
def checkMagazine(magazine, note):
    n=Counter(note)
    m=Counter(magazine)
    
    for i in note:
        if i in m and m[i]>0:
            m[i]-=1
            #print(i,m,n)
        else:
            return "No"
        
    return "Yes"
    
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
