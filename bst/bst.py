class BinaryTree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None



#Inserts at left side if node < parent or at right side if node > parent, unbalanced insertion
    def insert(self,data):
        if self.data is None: self.data = BinaryTree(data)
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = BinaryTree(data)
            if data > self.data:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = BinaryTree(data)

#Preorder traversal using recursion (ROOT-LEFT-RIGHT)
    def preorder_recursion(self):
        if self.data is None: return False
        if self.left:
            self.left.preorder_recursion()
        if self.right:
            self.right.preorder_recursion()

#Preorder using stack
    def preorder_stack(self):
        if self.data is None: return False
        res,stack = [],[self]
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.right)
                stack.append(node.left)

#Inorder traversal using recursion (LEFT-ROOT-RIGHT)
    def inorder_recursion(self):
        if self.data is None: return False
        if self.left:
            self.left.inorder_recursion()
        if self.right:
            self.right.inorder_recursion()

#Inorder using stack
    def inorder_stack(self):
        if self.data is None: return False
        stack = []
        while stack or self:
            if self:
                stack.append(self)
                self = self.left
            else:
                node = stack.pop()
                self = node.right

#Postorder traversal using reursion (LEFT-RIGHT-ROOT)
    def postorder_recursion(self):
        if self.data is None: return False
        if self.left:
            self.left.postorder_recursion()
        if self.right:
            self.right.postorder_recursion()

#Returns given node and it's parent ( used as a helper function for remove )
    def search(self,data,parent=None):
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.search(data,self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.search(data,self)
        else:
            return self,parent

    def children_count(self):
        return 0 if self.left is None and self.right is None else (2 if self.left and self.right else 1)

    def remove(self,data):
        node,parent = self.search(data)
        if node: ch_count = node.children_count()

#When node is a leaf (has no children), replace the pointer of it`s parent to None
        if ch_count == 0:
            if parent:
                if parent.left is node:
                    parent.left = None
                elif parent.right is node:
                    parent.right = None
                del node

#When node has 1 child, store pointer to node`s child in a temporary variable (t)
#and make replace the parent pointer to node with the temp variable t.
#If node is a root node then make left and right point to node`s children and set its
#own value to t.

        elif ch_count == 1:
            if node.left:
                t = node.left
            else:
                t = node.right
            if parent:
                if parent.left is node:
                    parent.left = t
                else:
                    parent.right = t
                del node

            else:
                self.right = t.right
                self.left = t.left
                self.data = t.data

#If node has 2 children, we will want to replace it with the lowest value to the right of the node.
#We set a slow and a fast pointer in the direction of right subtree going for the lowest value, when the lowest
#value is found, we replace the data at node with it. After we make the parent of the lowest value in
#right subtree skip over the lowest val.
        else:
            parent = node
            next = node.right
            while next.left:
                parent = next
                next = next.left
            node.data = next.data
            if parent.left == next:
                parent.left = next.right
            else:
                parent.right = next.right

#max_sum_path is a function that reunts the path of maximum sums between two leafs, height is a helper method to return highest sum path for each side.
    def height(self,root):
        return max(root.data+self.height(root.left),root.data+self.height(root.right)) if root else 0

    def max_sum_path(self,root):
        if root is None: return 0

        lh = self.height(root.left)
        rh = self.height(root.right)

        ld = self.max_sum_path(root.left)
        rd = self.max_sum_path(root.right)

        return max(lh+rh+root.data,max(ld,rd))
