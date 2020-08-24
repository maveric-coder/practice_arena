def minn(arr):
    min_dif = abs(arr[0]-arr[1])
    ans = []
    for i in range(len(arr)-1):
        d = abs(arr[i]-arr[i+1])
        if d==min_dif:
            ans += [arr[i], arr[i+1]]
            min_dif =d
        elif d<min_dif:
            ans = [arr[i], arr[i+1]]
            min_dif =d
    return ans


_=input()
ls=[int(x) for x in input().split()]
ls.sort()
print(*minn(ls))
