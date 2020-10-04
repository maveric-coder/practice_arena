def pairs(k, arr):
    ls=set(arr)
    return sum(1 for i in ls if i+k in ls)
