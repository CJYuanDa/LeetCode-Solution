from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # point to the last element of nums1 (exclude 0)
        p1 = m - 1
        # point to the last element of nums2
        p2 = n - 1
        # point to the last element of nums1 (include 0)
        p = m + n - 1

        # iterate from right to left (merge from the end)
        while p1 >= 0 and p2 >= 0:
            # compare the last element of nums1 and nums2
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
            
        # If there are remaining elements in nums2
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1