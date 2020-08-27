def getNode(head, position):
    count=0
    p = head
    while head.next:
        head=head.next
        count+=1
    i=0
    while i<count-position:
        p=p.next
        i+=1
    return p.data
