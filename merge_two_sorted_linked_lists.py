def mergeLists(headA, headB):
    if headA is None and headB is None:
        return None
  
    if headA is None:
        return headB

    if headB is None:
        return headA
  
    head = None
    if headA.data < headB.data :
        head = headA
        headA = headA.next
    else:
        head = headB
        headB = headB.next
    
    

    n = head
    while (headA != None and headB != None) :
        if (headA.data < headB.data):
            n.next = headA
            headA = headA.next
        else:
            n.next = headB
            headB = headB.next
        
        n = n.next
    
    if (headA == None):
        n.next = headB
    else:
        n.next = headA
    

    return head
