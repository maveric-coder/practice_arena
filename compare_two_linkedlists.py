def compare_lists(llist1, llist2):
    p=llist1
    q=llist2
    while p is not None:
        if q.data!=p.data or (p.next is None and q.next is not None) or (q.next is None and p.next is not None):
            return 0

        else:
            p=p.next
            q=q.next
    return 1
