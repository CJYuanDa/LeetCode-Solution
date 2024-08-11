from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = {}
        for index, num in nums.items():
            if num in hash.keys():
                if index - hash[num] == k:
                    return True
                hash[num] = index
            
            hash[num] = index
        
        return False
    
    def containsNearbyDuplicate1(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
                
            if nums[R] in window:
                return True
            
            window.add(nums[R])

        
        return False
