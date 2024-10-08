# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int: # type: ignore

        def dfs(node, is_left):
            if not node: return 0
            if not node.left and not node.right and is_left:
                return node.val
            
            return dfs(node.left, True) + dfs(node.right, False)
        
        return dfs(root, False)
    

    def sumOfLeftLeaves1(self, root: Optional[TreeNode]) -> int: # type: ignore
        self.ans = 0

        def dfs(node, is_left):
            if not node: return
            if not node.left and not node.right and is_left:
                self.ans += node.val
                return

            dfs(node.left, True)
            dfs(node.right, False)
        
        dfs(root, False)
        return self.ans