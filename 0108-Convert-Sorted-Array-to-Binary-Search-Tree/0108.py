# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]: # type: ignore

        def helper(L, R):
            if L > R: return None
            M = (L + R) // 2
            root = TreeNode(nums[M])
            root.left = helper(L, M - 1)
            root.right = helper(M + 1, R)
            return root
        
        return helper(0, len(nums) - 1)


            
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right