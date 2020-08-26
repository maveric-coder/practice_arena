def insertNodeAtPosition(head, data, position):
    d=SinglyLinkedListNode(data)
    d.next=None
    if head is None:
        head=d
        return d
    else:
        p=head
        i=0
        while i<position-1:
            p=p.next
            i+=1
        d.next=p.next
        p.next=d
        return head
