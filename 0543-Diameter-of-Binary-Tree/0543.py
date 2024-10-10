# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: # type: ignore
        self.ans = 0

        def find_height(node):
            if not node: return 0

            left = find_height(node.left)
            right = find_height(node.right)
            height = max(left, right)

            # check the maxium diameter
            self.ans = max(self.ans, left + right)

            return 1 + height

        find_height(root)

        return self.ans