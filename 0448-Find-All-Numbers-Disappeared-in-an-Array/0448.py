from ast import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            # get the num and mark the index corresponding to its value as negative
            # therefore all nums will be negative except missing number (missing index)
            index = abs(num) - 1
            nums[index] = - abs(nums[index])
        
        for i in range(len(nums)):
            # if num > 0, it means this index is missing num.
            if nums[i] > 0:
                ans.append(i + 1)
        
        return ans