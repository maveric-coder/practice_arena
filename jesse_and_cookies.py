def cookies(k, A):
    from heapq import heappop,heappush,heapify

    heapify(A)
    fC = 0
    try:
        while A[0] < k:
            fC+=1
            c1 = heappop(A)
            c2 = heappop(A)
            newCookie=(1*c1)+(2*c2)
            heappush(A,newCookie)
        return fC
    except:
        return -1
    
