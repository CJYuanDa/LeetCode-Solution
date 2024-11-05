from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        count = 0

        for num in nums:
            if num == 0:
                count = 0
            else:
                count += 1
        
            if count > ans:
                ans = count

        return ans