from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k: the index point to the value which is not equal to val
        k = 0
        for num in nums:
            if num != val:
                # reset the array
                nums[k] = num
                k += 1
        return k
            