# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from scipy import stats
n=int(input())
ls=[int(x) for x in input().split()]
print(np.mean(ls))
print(np.median(ls))
print(int(stats.mode(ls)[0]))

