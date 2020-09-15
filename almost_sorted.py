#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def almostSorted(arr):
    ls=sorted(arr)
    i=0
    f=1
    st=[]
    c=0
    xt=[]
    if ls==arr:
        print( "yes")
        return 0
    for i in range(len(ls)):
        if ls[i]!=arr[i]:
            st.append(i+1)

            c+=1
    if c==2:
        print("yes")
        print("swap",*st)
        return 0
    else :
        for i in range(len(arr)):
            if arr[i]==ls[i]:
                None
            else:
                xt.append(arr[i])
        if xt==sorted(xt,reverse=True):
            print("yes")
            print("reverse", arr.index(xt[0])+1,arr.index(xt[-1])+1)
            return 0

    print("no")
    return 0
        

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
