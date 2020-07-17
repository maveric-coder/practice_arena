# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
for _ in (range(int(input()))):
    input()
    side_lengths = deque(map(int, input().strip().split()))
    result = "Yes"
    if max(side_lengths) not in (side_lengths[0], side_lengths[-1]):
        result = "No"
    print(result)
