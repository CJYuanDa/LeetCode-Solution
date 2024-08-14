from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
                i -= 1

    def moveZeroes1(self, nums: List[int]) -> None:
        # two pointers: zero(z) and none zero(n_z)
        z = 0
        for n_z in range(len(nums)):
            # if none zero pointer point to the none zero value
            if nums[n_z] != 0:
                swap = nums[z]
                nums[z] = nums[n_z]
                nums[n_z] = swap
                z += 1
