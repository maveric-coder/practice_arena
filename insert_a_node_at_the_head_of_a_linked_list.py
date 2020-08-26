def insertNodeAtHead(llist, data):
    # Write your code here
    d=SinglyLinkedListNode(data)
    d.next=llist
    llist=d
    return llist
