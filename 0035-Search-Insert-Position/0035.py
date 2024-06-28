from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index, value in enumerate(nums):
            if target <= value:
                return index
        
        return len(nums)
    
# binary search
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            else:
                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        if left > right:
            return left
        else: 
            return right