def deleteNode(head, position):
    if head is None:
        return None
    elif position==0:
        head=head.next
        return head
    else:
        p=head
        b=None
        i=0
        while i<position:
            b=p
            p=p.next
            i+=1
        b.next=p.next
        p.next=None
        return head
