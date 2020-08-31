def postOrder(root):
    #Write your code here
    if root is None:
        return 
    else:
        postOrder(root.left)
        postOrder(root.right)
        print(root,end=" ")
