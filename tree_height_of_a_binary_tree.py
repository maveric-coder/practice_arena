def height(root):
    m=0
    x=0
    if root is None:
        return 
    else:
        if root.left:
            m=1+height(root.left)
        if root.right:
            x=1+height(root.right)
        return(max(m,x))
