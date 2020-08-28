

n=int(input())
ls=[int(x) for x in input().split()]
f=[int(x) for x in input().split()]
print (round(1.0 * sum([ls[i]*f[i] for i in range (n)])/sum(f),1))
