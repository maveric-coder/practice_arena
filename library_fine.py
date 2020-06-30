from datetime import date
d1,m1,y1=map(int,input().split())
d2,m2,y2=map(int,input().split())
fine=0
y=y1-y2
if y<0:
    y=0
m=m1-m2
if m<0 or y>0 or y1<y2:
    m=0
d=d1-d2
if d<0 or y>0 or m>0 or y1<y2 or m1<m2:
    d=0
fine=(15*d)+(500*m)+(10000*y)
print(fine)

