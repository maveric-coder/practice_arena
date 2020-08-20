#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.
def gridChallenge(grid):
    i=0
    while i<len(grid)-1 :
        
        s=sorted(grid[i])
        t=sorted(grid[i+1])
        for j in range(len(grid[0])):
            if s[j]>t[j]:
                return ("NO")
        i+=1
    return ("YES")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
