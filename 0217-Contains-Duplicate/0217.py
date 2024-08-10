from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}

        for num in nums:
            if num in hash.keys():
                return True

            hash[num] = 1
        
        return False
        
    def containsDuplicate1(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))