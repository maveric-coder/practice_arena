h=int(input())
m=int(input())
ls=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine"]

st=["o' clock", "quarter past","half past","quarter to"]

sm=""
if m%15==0:
    sm=st[int(m/15)]
    if int(m/15)==3:
        h+=1
else:
    if m==1:
        sm=ls[m]+" minute past"
    elif m<=30:
        sm=ls[m]+" minutes past"
    else:
        sm=ls[60-m]+" minutes to"
        h+=1

sh=ls[h]
if m/15==0:
    print(sh,sm)
else:
    print(sm,sh)

