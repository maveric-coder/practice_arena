# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    return min([arr[x+k-1]-arr[x] for x in range(n-k+1)])
