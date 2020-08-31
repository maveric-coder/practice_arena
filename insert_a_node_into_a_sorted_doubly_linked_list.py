def sortedInsert(head, data):
    bb=DoublyLinkedListNode(data)
    bb.next=None
    bb.prev=None
    if head is None:
        return bb
    elif data<head.data:
        bb.next=head
        head.prev=bb
        return bb
    else:
        bb=sortedInsert(head.next,data)
        head.next=bb
        bb.prev=head
        return head
