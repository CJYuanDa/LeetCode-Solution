from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first, second, third = None, None, None

        for num in nums:
            # Skip the number if it's already considered as one of the top 3 maxes
            if first == num or second == num or third == num:
                continue

            if first is None or num > first:
                third = second
                second = first
                first = num
            elif second is None or num > second:
                third = second
                second = num
            elif third is None or num > third:
                third = num

        return third if third is not None else first