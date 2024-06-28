from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = len(digits) - 1

        # iterate from left to right
        while idx >= 0:
            sum = digits[idx] + 1
            if sum < 10:
                digits[idx] = sum
                return digits
            else:
                digits[idx] = 0
                idx -= 1

        # means the first number of original array is greater than 9, therefor insert value 1 in 0 index
        digits.insert(0, 1)

        return digits