class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int: # type: ignore
        self.prev = None # To track the previous node's value
        self.min = 10 ** 5

        # In-order traversal: left -> current -> right
        def inorder(node):
            if not node: return

            inorder(node.left)

            # Calculate difference with the previous node
            if self.prev is not None:
                self.min = min(self.min, node.val - self.prev)
            
            self.prev = node.val

            inorder(node.right)
        
        inorder(root)

        return self.min