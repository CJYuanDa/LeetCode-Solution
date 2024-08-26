from typing import Counter, List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = Counter(nums1)
        res = []

        for num in nums2:
            if num in hash.keys() and hash[num] > 0:
                res.append(num)
                hash[num] -= 1
        
        return res

    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        i = 0
        j = 0
        res = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:  # nums1[i] == nums2[j]
                res.append(nums1[i])
                i += 1
                j += 1
        
        return res