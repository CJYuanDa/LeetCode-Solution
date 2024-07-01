from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        
        # iterate start from index 1 (left -> right)
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        return k + 1