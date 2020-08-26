def reverse(head):
    if head is None:
        return None
    prev=None
    cur=head
    aux=head.next
    while cur is not None:
        cur.next=prev
        prev=cur
        cur=aux
        if cur is not None:
            aux=aux.next
    return prev
