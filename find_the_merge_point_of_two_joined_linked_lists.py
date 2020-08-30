def findMergeNode(h1, h2):
    a=h1
    b=h2
    while a.next!=None:
        temp=a
        a=a.next
        temp.next=None
    while b.next!=None:
        b=b.next
    return b.data
