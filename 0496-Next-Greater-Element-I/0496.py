from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            i = nums2.index(num)
            next = i + 1
            check = 0
            while next < len(nums2):
                if nums2[next] > num:
                    ans.append(nums2[next])
                    check = 1
                    break
                next += 1
            
            if check == 0:
                ans.append(-1)

        return ans
    
    def nextGreaterElement1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1 = {value : index for index, value in enumerate(nums1)}
        ans = [-1] * len(nums1)
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                index = map1[stack.pop()]
                ans[index] = num

            if num in map1:
                stack.append(num)

        return ans