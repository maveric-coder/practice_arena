def b(n):
    return(bin(n).count('1'))
for _ in range(int(input())):
    n=int(input())
    ls=[int(x) for x in input().split()]
    ls.sort(key=b)
    print(' '.join(map(str,ls)))
    
