def inOrder(root):
    #Write your code here
    if root is None:
        return
    else:
        
        if root.left:
            inOrder(root.left)
        print(root,end=" ")
        if root.right:
            inOrder(root.right)
