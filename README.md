# python_practice
It contains solution to few of the HackeRank problems I've solved till now using Python. It's updated often.

Check out my HackerRank Profile at: https://www.hackerrank.com/anand_kumar15

## Link List
```python
class node:
    def __init__(self,val):
        self.val=val
        self.next=None
  

 
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.head=None
        self.ls=[]
        
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        
        if index<len(self.ls):
            return self.ls[index].val
        else:
            return -1
            
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        
        newNode=node(val)
        newNode.next=self.head
        self.head=newNode
        self.ls.insert(0,self.head)
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list
        """
        newNode=node(val)
        if len(self.ls)==0:
            self.ls.append(newNode)
            self.head=newNode
            return
        
        lastnode=self.ls[len(self.ls)-1]
        lastnode.next=newNode
        self.ls.append(newNode)
            
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        newNode=node(val)
        if index==0:
            self.ls.insert(index,newNode)
            newNode.next=self.head
            self.head=newNode
            return
        prevnode=self.ls[index-1]
        nextnode=prevnode.next
        prevnode.next=newNode
        newNode.next=nextnode
        self.ls.insert(index,newNode)
        
        
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index<len(self.ls):
            if index==0:
                deletenode=self.head
                deletenode.next=None
                self.head=self.head.next
                self.ls.pop(index)
                return
            prevnode=self.ls[index-1]
            deletenode=prevnode.next
            prevnode.next=deletenode.next
            deletenode.next=None
            self.ls.pop(index)
