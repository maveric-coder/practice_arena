def countingNumbers(arr,d):
    count=[0]*201
    size=d
    for i in range(size):
        count[arr[i]]+=1
    return count
def updating(arr,count,beg,end):
    count[arr[beg]]-=1
    count[arr[end]]+=1
    cumfreq=[val for val in count]
    for i in range(1,201):
        cumfreq[i] += cumfreq[i - 1]
    return cumfreq
def getMedian(cumfreq, d):
    if d%2==0:
        middle1= d//2
        middle2 = middle1 + 1
        i=0
        j=0
        while cumfreq[i]<middle1:
            i+=1
        firstItem = i
        while cumfreq[j]<middle2:
            j+=1
        secondItem = j
        median=(firstItem+secondItem)/2
        return median
    else:
        middle=(d+1)//2
        i=0
        while cumfreq[i]<middle:
            i+=1
        median = i
        return median

def  activityNotifications(expenditure,d):
   beg=0
   end=d
   notification=0
   length=len(expenditure)
   count=countingNumbers(expenditure,d)
   cumfreq = updating(expenditure, count, -1,-1)
   while end<length:
       if expenditure[end]>=2*getMedian(cumfreq,d):
           notification+=1
       cumfreq=updating(expenditure,count,beg,end)
       beg+=1
       end+=1
   return notification


    
_,n=map(int,input().split())
ls=[int(x) for x in input().split()]
print(activityNotifications(ls,n))
