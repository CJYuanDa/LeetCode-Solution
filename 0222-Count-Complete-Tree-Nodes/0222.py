# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int: # type: ignore
        if not root: 
            return 0

        left = self.left_height(root)
        right = self.right_height(root)
        
        if left > right:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        else:
            return 2 ** left - 1
        
    def left_height(self, node):
        if not node: 
            return 0
        return 1 + self.left_height(node.left)

    def right_height(self,node):
        if not node: 
            return 0
        return 1 + self.right_height(node.right)