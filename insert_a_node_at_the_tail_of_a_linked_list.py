def insertNodeAtTail(head, data):
    d=SinglyLinkedListNode(data)
    d.next=None
    if head is None:
        head=d
        return head
    else:
        p=head
        while p.next is not None:
            p=p.next
        p.next=d
        return head
