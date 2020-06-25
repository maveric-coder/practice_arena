ls = [int(x) for x in input().split()]
n = ls[0]
k = ls[1]
queries = ls[2]
array = [int(x) for x in input().split()]
result = []
for q in range(queries):
    q = int(input())
    result.append(array[q-k % n])
for e in result:
    print(e)
