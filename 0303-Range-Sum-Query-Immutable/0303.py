from typing import List

class NumArray:

    # nums:       [1,2,-3,0,4]
    # prefix_sum: [1,3,0,0,4]
    # sumRange = prefix_sum[right] - prefix_sum[left - 1]
    
    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        sum = 0
        for num in nums:
            sum += num
            self.prefix_sum.append(sum)

    def sumRange(self, left: int, right: int) -> int:
        right = self.prefix_sum[right]
        left = self.prefix_sum[left - 1] if left > 0 else 0
        return  right - left



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)