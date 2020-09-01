    def insert(self, val):
        n=self.root
        if not n:
            self.root=Node(val)
            return self.root
        while n:
            if n.info>val:
                if n.left:
                    n=n.left
                else:
                    n.left=Node(val)
                    break
            else:
                if n.right:
                    n = n.right
                else:
                    n.right = Node(val)
                    break
        return self.root
