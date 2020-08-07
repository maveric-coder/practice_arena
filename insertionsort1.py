
# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    
    i = n-1
    val = arr[i]
    while(i>0 and val<arr[i-1]):
        arr[i] = arr[i-1]
        print(*arr)
        i-=1
    arr[i] = val
    print(*arr)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
