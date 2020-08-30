def has_cycle(head):
    if head==None or head.next is None:
        return False
    p=head
    for i in range(1000):
        if p.next is None:
            return False
        else:
            p=p.next
    return True
