from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashset = set(nums1)
        res = []

        for num in nums2:
            if num in hashset:
                res.append(num)
                hashset.remove(num)
        
        return res
