from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        nums.sort()
        for index, num in enumerate(nums):
            if index != num:
                return index
            
        return -1
    
    def missingNumber1(self, nums: List[int]) -> int:
        n = len(nums)

        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)

        return expected_sum - actual_sum