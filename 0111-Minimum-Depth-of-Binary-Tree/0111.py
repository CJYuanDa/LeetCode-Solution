# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int: # type: ignore
        
        def min_height(root):
            if not root: return 0

            left = min_height(root.left)
            right = min_height(root.right)

            if left > 0 and right > 0:
                return 1 + min(left, right)
            elif left > 0:
                return 1 + left
            else:
                return 1 + right

        return min_height(root)