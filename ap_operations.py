# Write your code here
for _ in range(int(input())):

    a, b, c = map(int, input().split())

#print(a, b, c)

    print((abs((b-a)-(c-b))+1)//2)
