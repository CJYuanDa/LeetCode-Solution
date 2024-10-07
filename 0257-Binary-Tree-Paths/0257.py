# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]: # type: ignore
        ans = []
        if not root: return ans

        def tree_path(node, path):
            path += str(node.val)

            if not node.left and not node.right:
                ans.append(path)
                return
            
            if node.left:
                tree_path(node.left, path + "->")
            
            if node.right:
                tree_path(node.right, path + "->")
        
        tree_path(root, "")
        return ans